from datetime import UTC, datetime

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.curriculum import Lesson, QuizQuestion
from app.models.notes import Bookmark, LearningNote
from app.models.progress import ExerciseAttempt, LessonProgress, QuizAttempt
from app.models.project import LearningActivity, MilestoneVerification
from app.schemas.dashboard import DashboardSummaryOut, DashboardTodayLesson
from app.schemas.project import LearningActivityOut, MilestoneVerificationOut
from app.schemas.quiz import QuizAnswerResult, QuizAnswerSubmit, QuizBatchResult


def utc_now() -> datetime:
    return datetime.now(UTC)


async def update_lesson_status(
    db: AsyncSession, user_id: str, day_or_id: str, new_status: str
) -> LessonProgress:
    # Resolve lesson
    if day_or_id.isdigit():
        stmt = select(Lesson).where(Lesson.day_number == int(day_or_id))
    else:
        stmt = select(Lesson).where(Lesson.id == day_or_id)
    lesson = (await db.execute(stmt)).scalar_one_or_none()
    if not lesson:
        raise ValueError(f"Lesson '{day_or_id}' not found.")

    # Validate transition
    valid_statuses = {"not_started", "in_progress", "completed"}
    if new_status not in valid_statuses:
        raise ValueError(f"Invalid status '{new_status}'. Must be one of {valid_statuses}")

    prog_stmt = select(LessonProgress).where(
        LessonProgress.user_id == user_id, LessonProgress.lesson_id == lesson.id
    )
    prog = (await db.execute(prog_stmt)).scalar_one_or_none()

    now = utc_now()
    if not prog:
        prog = LessonProgress(
            user_id=user_id,
            lesson_id=lesson.id,
            day_number=lesson.day_number,
            status=new_status,
            started_at=now if new_status in ("in_progress", "completed") else None,
            completed_at=now if new_status == "completed" else None,
            last_accessed_at=now,
        )
        db.add(prog)
    else:
        prog.status = new_status
        prog.last_accessed_at = now
        if new_status in ("in_progress", "completed") and not prog.started_at:
            prog.started_at = now
        if new_status == "completed" and not prog.completed_at:
            prog.completed_at = now
        elif new_status != "completed":
            prog.completed_at = None

    # Log learning activity
    activity = LearningActivity(
        user_id=user_id,
        activity_type=f"lesson_{new_status}",
        day_number=lesson.day_number,
        summary=f"Marked Day {lesson.day_number} ({lesson.title}) as {new_status.replace('_', ' ').title()}",
        metadata_json={"lesson_id": lesson.id, "new_status": new_status},
        created_at=now,
    )
    db.add(activity)

    await db.commit()
    await db.refresh(prog)
    return prog


async def get_dashboard_summary(db: AsyncSession, user_id: str) -> DashboardSummaryOut:
    # Source-of-truth counts directly from database
    total_days = 112

    # Completed count
    comp_stmt = select(func.count(LessonProgress.id)).where(
        LessonProgress.user_id == user_id, LessonProgress.status == "completed"
    )
    completed_days = (await db.execute(comp_stmt)).scalar() or 0

    # In progress count
    prog_stmt = select(func.count(LessonProgress.id)).where(
        LessonProgress.user_id == user_id, LessonProgress.status == "in_progress"
    )
    in_progress_days = (await db.execute(prog_stmt)).scalar() or 0

    remaining_days = max(0, total_days - completed_days)
    completion_percentage = round((completed_days / total_days) * 100.0, 1)

    # Determine current day: first not_started or in_progress lesson
    # Fetch all completed day numbers
    completed_day_nums = set(
        (
            await db.execute(
                select(LessonProgress.day_number).where(
                    LessonProgress.user_id == user_id,
                    LessonProgress.status == "completed",
                )
            )
        )
        .scalars()
        .all()
    )

    current_day_number = 1
    for day in range(1, 113):
        if day not in completed_day_nums:
            current_day_number = day
            break

    # Current week and phase based on current day
    current_week = ((current_day_number - 1) // 7) + 1
    if current_day_number <= 28:
        current_phase = 1
    elif current_day_number <= 70:
        current_phase = 2
    elif current_day_number <= 98:
        current_phase = 3
    else:
        current_phase = 4

    # Fetch today lesson details
    lesson_stmt = select(Lesson).where(Lesson.day_number == current_day_number)
    today_lesson_rec = (await db.execute(lesson_stmt)).scalar_one_or_none()

    today_lesson_out = None
    if today_lesson_rec:
        status_stmt = select(LessonProgress.status).where(
            LessonProgress.user_id == user_id,
            LessonProgress.lesson_id == today_lesson_rec.id,
        )
        t_status = (await db.execute(status_stmt)).scalar() or "not_started"
        today_lesson_out = DashboardTodayLesson(
            id=today_lesson_rec.id,
            day_number=today_lesson_rec.day_number,
            week_number=today_lesson_rec.week_number,
            phase_number=today_lesson_rec.phase_number,
            title=today_lesson_rec.title,
            summary=today_lesson_rec.summary,
            duration_minutes=today_lesson_rec.duration_minutes,
            status=t_status,
        )

    # Weekly milestones
    m_stmt = (
        select(MilestoneVerification)
        .where(MilestoneVerification.user_id == user_id)
        .order_by(MilestoneVerification.week_number)
    )
    milestones = (await db.execute(m_stmt)).scalars().all()
    weekly_milestones_out = [
        MilestoneVerificationOut(
            week_number=m.week_number,
            status=m.status,
            evidence_notes=m.evidence_notes,
            verified_at=m.verified_at,
        )
        for m in milestones
    ]

    # Recent activities (up to 10)
    act_stmt = (
        select(LearningActivity)
        .where(LearningActivity.user_id == user_id)
        .order_by(LearningActivity.created_at.desc())
        .limit(10)
    )
    activities = (await db.execute(act_stmt)).scalars().all()
    recent_activities_out = [
        LearningActivityOut(
            id=a.id,
            activity_type=a.activity_type,
            day_number=a.day_number,
            summary=a.summary,
            created_at=a.created_at,
        )
        for a in activities
    ]

    # Bookmarks count
    bm_count_stmt = select(func.count(Bookmark.id)).where(Bookmark.user_id == user_id)
    bookmarked_count = (await db.execute(bm_count_stmt)).scalar() or 0

    # Notes count
    notes_count_stmt = select(func.count(LearningNote.id)).where(LearningNote.user_id == user_id)
    notes_count = (await db.execute(notes_count_stmt)).scalar() or 0

    return DashboardSummaryOut(
        current_day=current_day_number,
        current_week=current_week,
        current_phase=current_phase,
        total_days=total_days,
        completed_days=completed_days,
        in_progress_days=in_progress_days,
        remaining_days=remaining_days,
        completion_percentage=completion_percentage,
        today_lesson=today_lesson_out,
        weekly_milestones=weekly_milestones_out,
        recent_activities=recent_activities_out,
        bookmarked_count=bookmarked_count,
        notes_count=notes_count,
    )


async def submit_exercise_attempt(
    db: AsyncSession,
    user_id: str,
    lesson_id: str,
    exercise_id: str,
    submitted_output: str,
    notes: str | None = None,
) -> ExerciseAttempt:
    now = utc_now()
    attempt = ExerciseAttempt(
        user_id=user_id,
        lesson_id=lesson_id,
        exercise_id=exercise_id,
        status="passed",
        submitted_output=submitted_output,
        notes=notes,
        attempted_at=now,
    )
    db.add(attempt)

    # Activity
    act = LearningActivity(
        user_id=user_id,
        activity_type="exercise_completed",
        day_number=int(lesson_id.split("-")[1]) if "-" in lesson_id else None,
        summary=f"Completed exercise '{exercise_id}' for {lesson_id}",
        metadata_json={"lesson_id": lesson_id, "exercise_id": exercise_id},
        created_at=now,
    )
    db.add(act)

    await db.commit()
    await db.refresh(attempt)
    return attempt


async def evaluate_quiz_answers(
    db: AsyncSession,
    user_id: str,
    lesson_id: str,
    answers: list[QuizAnswerSubmit],
) -> QuizBatchResult:
    # Get questions
    q_ids = [a.question_id for a in answers]
    stmt = select(QuizQuestion).where(QuizQuestion.id.in_(q_ids))
    questions = (await db.execute(stmt)).scalars().all()
    q_map = {q.id: q for q in questions}

    results: list[QuizAnswerResult] = []
    correct_count = 0
    now = utc_now()

    for ans in answers:
        q = q_map.get(ans.question_id)
        if not q:
            continue

        is_correct = ans.selected_answer.strip() == q.correct_answer.strip()
        if is_correct:
            correct_count += 1

        # Record attempt
        attempt = QuizAttempt(
            user_id=user_id,
            lesson_id=lesson_id,
            question_id=q.id,
            selected_answer=ans.selected_answer,
            is_correct=is_correct,
            score=1 if is_correct else 0,
            attempted_at=now,
        )
        db.add(attempt)

        results.append(
            QuizAnswerResult(
                question_id=q.id,
                selected_answer=ans.selected_answer,
                correct_answer=q.correct_answer,
                is_correct=is_correct,
                explanation=q.explanation,
            )
        )

    total_q = len(answers)
    score_pct = round((correct_count / total_q) * 100.0, 1) if total_q > 0 else 0.0

    day_num = int(lesson_id.split("-")[1]) if "-" in lesson_id else 0

    # Activity
    act = LearningActivity(
        user_id=user_id,
        activity_type="quiz_completed",
        day_number=day_num,
        summary=f"Completed Day {day_num} Quiz: {correct_count}/{total_q} correct ({score_pct}%)",
        metadata_json={"lesson_id": lesson_id, "score_percentage": score_pct},
        created_at=now,
    )
    db.add(act)

    await db.commit()

    return QuizBatchResult(
        lesson_id=lesson_id,
        day_number=day_num,
        total_questions=total_q,
        correct_count=correct_count,
        score_percentage=score_pct,
        results=results,
    )
