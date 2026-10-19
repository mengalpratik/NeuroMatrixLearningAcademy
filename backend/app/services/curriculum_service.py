from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.curriculum import CurriculumPhase, CurriculumWeek, Lesson
from app.models.notes import Bookmark, LearningNote
from app.models.progress import LessonProgress
from app.models.project import MilestoneVerification
from app.schemas.curriculum import (
    CodeExample,
    CommonError,
    ConceptSection,
    CurriculumOverviewOut,
    Exercise,
    LessonDetailOut,
    LessonSummaryOut,
    NeuroMatrixIntegration,
    PhaseOverviewOut,
    QuizQuestionOut,
    WeekOverviewOut,
)


async def get_curriculum_overview(db: AsyncSession, user_id: str) -> CurriculumOverviewOut:
    # Fetch phases with weeks and lessons
    phase_stmt = (
        select(CurriculumPhase)
        .options(selectinload(CurriculumPhase.weeks).selectinload(CurriculumWeek.lessons))
        .order_by(CurriculumPhase.phase_number)
    )
    phases = (await db.execute(phase_stmt)).scalars().all()

    # Fetch user progress map
    prog_stmt = select(LessonProgress).where(LessonProgress.user_id == user_id)
    progress_records = (await db.execute(prog_stmt)).scalars().all()
    status_map = {p.lesson_id: p.status for p in progress_records}

    # Fetch user bookmarks map
    bm_stmt = select(Bookmark.lesson_id).where(Bookmark.user_id == user_id)
    bookmarked_ids = set((await db.execute(bm_stmt)).scalars().all())

    # Fetch user notes map
    notes_stmt = select(LearningNote.lesson_id).where(LearningNote.user_id == user_id)
    noted_ids = set((await db.execute(notes_stmt)).scalars().all())

    # Fetch weekly milestone statuses
    m_stmt = select(MilestoneVerification).where(MilestoneVerification.user_id == user_id)
    milestones = (await db.execute(m_stmt)).scalars().all()
    m_status_map = {m.week_number: m.status for m in milestones}

    phases_out: list[PhaseOverviewOut] = []
    total_completed = 0
    total_in_progress = 0

    for phase in phases:
        weeks_out: list[WeekOverviewOut] = []
        for week in sorted(phase.weeks, key=lambda w: w.week_number):
            lessons_out: list[LessonSummaryOut] = []
            for lesson in sorted(week.lessons, key=lambda l: l.day_number):
                status = status_map.get(lesson.id, "not_started")
                if status == "completed":
                    total_completed += 1
                elif status == "in_progress":
                    total_in_progress += 1

                lessons_out.append(
                    LessonSummaryOut(
                        id=lesson.id,
                        day_number=lesson.day_number,
                        week_number=lesson.week_number,
                        phase_number=lesson.phase_number,
                        title=lesson.title,
                        slug=lesson.slug,
                        summary=lesson.summary,
                        duration_minutes=lesson.duration_minutes,
                        status=status,
                        is_bookmarked=lesson.id in bookmarked_ids,
                        has_notes=lesson.id in noted_ids,
                    )
                )

            weeks_out.append(
                WeekOverviewOut(
                    week_number=week.week_number,
                    phase_number=week.phase_number,
                    title=week.title,
                    days_range=week.days_range,
                    summary=week.summary,
                    milestone_title=week.milestone_title,
                    milestone_description=week.milestone_description,
                    milestone_criteria=week.milestone_criteria or [],
                    milestone_status=m_status_map.get(week.week_number, "locked"),
                    lessons=lessons_out,
                )
            )

        phases_out.append(
            PhaseOverviewOut(
                phase_number=phase.phase_number,
                title=phase.title,
                weeks_range=phase.weeks_range,
                days_range=phase.days_range,
                description=phase.description,
                focus_area=phase.focus_area,
                weeks=weeks_out,
            )
        )

    return CurriculumOverviewOut(
        phases=phases_out,
        total_days=112,
        completed_days=total_completed,
        in_progress_days=total_in_progress,
    )


async def get_lesson_by_day_or_id(
    db: AsyncSession, user_id: str, identifier: str
) -> LessonDetailOut | None:
    if identifier.isdigit():
        day_num = int(identifier)
        stmt = (
            select(Lesson).options(selectinload(Lesson.quizzes)).where(Lesson.day_number == day_num)
        )
    else:
        stmt = select(Lesson).options(selectinload(Lesson.quizzes)).where(Lesson.id == identifier)

    lesson = (await db.execute(stmt)).scalar_one_or_none()
    if not lesson:
        return None

    # Fetch status
    prog_stmt = select(LessonProgress).where(
        LessonProgress.user_id == user_id, LessonProgress.lesson_id == lesson.id
    )
    prog = (await db.execute(prog_stmt)).scalar_one_or_none()
    status = prog.status if prog else "not_started"

    # Fetch bookmark
    bm_stmt = select(Bookmark).where(Bookmark.user_id == user_id, Bookmark.lesson_id == lesson.id)
    bm = (await db.execute(bm_stmt)).scalar_one_or_none()

    # Fetch current note
    note_stmt = (
        select(LearningNote)
        .where(LearningNote.user_id == user_id, LearningNote.lesson_id == lesson.id)
        .order_by(LearningNote.updated_at.desc())
    )
    note = (await db.execute(note_stmt)).scalar_one_or_none()

    # Navigation pointers
    prev_day = lesson.day_number - 1 if lesson.day_number > 1 else None
    next_day = lesson.day_number + 1 if lesson.day_number < 112 else None

    # Convert complex fields
    concepts = [ConceptSection(**c) for c in (lesson.concept_sections or [])]
    codes = [CodeExample(**c) for c in (lesson.code_examples or [])]
    exs = [Exercise(**e) for e in (lesson.exercises or [])]
    errs = [CommonError(**e) for e in (lesson.common_errors or [])]
    nm_int = NeuroMatrixIntegration(**(lesson.neuromatrix_integration or {}))

    quizzes_out = [
        QuizQuestionOut(
            id=q.id,
            day_number=q.day_number,
            question_text=q.question_text,
            question_type=q.question_type,
            code_snippet=q.code_snippet,
            options=q.options or [],
            explanation=q.explanation,
        )
        for q in (lesson.quizzes or [])
    ]

    return LessonDetailOut(
        id=lesson.id,
        day_number=lesson.day_number,
        week_number=lesson.week_number,
        phase_number=lesson.phase_number,
        title=lesson.title,
        slug=lesson.slug,
        summary=lesson.summary,
        duration_minutes=lesson.duration_minutes,
        objectives=lesson.objectives or [],
        prerequisites=lesson.prerequisites or [],
        revision_questions=lesson.revision_questions or [],
        concept_sections=concepts,
        code_examples=codes,
        exercises=exs,
        common_errors=errs,
        edge_cases=lesson.edge_cases or [],
        neuromatrix_integration=nm_int,
        completion_criteria=lesson.completion_criteria or [],
        quizzes=quizzes_out,
        status=status,
        is_bookmarked=bm is not None,
        current_note=note.content if note else None,
        prev_day=prev_day,
        next_day=next_day,
    )


async def search_lessons(
    db: AsyncSession,
    user_id: str,
    query: str | None = None,
    phase: int | None = None,
    status_filter: str | None = None,
    topic: str | None = None,
) -> list[LessonSummaryOut]:
    stmt = select(Lesson).order_by(Lesson.day_number)

    if phase:
        stmt = stmt.where(Lesson.phase_number == phase)

    if query:
        term = f"%{query.strip()}%"
        stmt = stmt.where(
            or_(
                Lesson.title.ilike(term),
                Lesson.summary.ilike(term),
                Lesson.slug.ilike(term),
            )
        )

    if topic:
        term = f"%{topic.strip()}%"
        stmt = stmt.where(Lesson.title.ilike(term))

    lessons = (await db.execute(stmt)).scalars().all()

    # Progress & bookmarks maps
    prog_stmt = select(LessonProgress).where(LessonProgress.user_id == user_id)
    progs = (await db.execute(prog_stmt)).scalars().all()
    status_map = {p.lesson_id: p.status for p in progs}

    bm_stmt = select(Bookmark.lesson_id).where(Bookmark.user_id == user_id)
    bm_set = set((await db.execute(bm_stmt)).scalars().all())

    results: list[LessonSummaryOut] = []
    for l in lessons:
        l_status = status_map.get(l.id, "not_started")
        if status_filter and status_filter != "all" and l_status != status_filter:
            continue

        results.append(
            LessonSummaryOut(
                id=l.id,
                day_number=l.day_number,
                week_number=l.week_number,
                phase_number=l.phase_number,
                title=l.title,
                slug=l.slug,
                summary=l.summary,
                duration_minutes=l.duration_minutes,
                status=l_status,
                is_bookmarked=l.id in bm_set,
                has_notes=False,
            )
        )

    return results
