import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.models.curriculum import CurriculumPhase, CurriculumWeek, Lesson, QuizQuestion
from app.models.project import MilestoneVerification, ProjectTask
from app.services.curriculum_data import get_all_curriculum_data

logger = logging.getLogger(__name__)


async def seed_curriculum(db: AsyncSession) -> None:
    """
    Seed curriculum phases, weeks, lessons, quizzes, and initial milestone/project tasks idempotently.
    Existing user progress and notes are strictly preserved.
    """
    data = get_all_curriculum_data()

    # 1. Seed Phases
    for p_data in data["phases"]:
        stmt = select(CurriculumPhase).where(CurriculumPhase.phase_number == p_data["phase_number"])
        existing = (await db.execute(stmt)).scalar_one_or_none()
        if not existing:
            phase = CurriculumPhase(**p_data)
            db.add(phase)
        else:
            existing.title = p_data["title"]
            existing.weeks_range = p_data["weeks_range"]
            existing.days_range = p_data["days_range"]
            existing.description = p_data["description"]
            existing.focus_area = p_data["focus_area"]

    await db.flush()

    # 2. Seed Weeks
    for w_data in data["weeks"]:
        stmt = select(CurriculumWeek).where(CurriculumWeek.week_number == w_data["week_number"])
        existing = (await db.execute(stmt)).scalar_one_or_none()
        if not existing:
            week = CurriculumWeek(**w_data)
            db.add(week)
        else:
            existing.title = w_data["title"]
            existing.days_range = w_data["days_range"]
            existing.summary = w_data["summary"]
            existing.milestone_title = w_data["milestone_title"]
            existing.milestone_description = w_data["milestone_description"]
            existing.milestone_criteria = w_data["milestone_criteria"]

    await db.flush()

    # 3. Seed Lessons (All 112 days)
    for l_data in data["lessons"]:
        stmt = select(Lesson).where(Lesson.id == l_data["id"])
        existing = (await db.execute(stmt)).scalar_one_or_none()
        if not existing:
            lesson = Lesson(**l_data)
            db.add(lesson)
        else:
            # Update content while keeping ID and relations
            for field, val in l_data.items():
                setattr(existing, field, val)

    await db.flush()

    # 4. Seed Quizzes
    for q_data in data["quizzes"]:
        stmt = select(QuizQuestion).where(QuizQuestion.id == q_data["id"])
        existing = (await db.execute(stmt)).scalar_one_or_none()
        if not existing:
            quiz = QuizQuestion(**q_data)
            db.add(quiz)
        else:
            for field, val in q_data.items():
                setattr(existing, field, val)

    await db.flush()

    # 5. Initialize Milestone Verifications (Weeks 1..16)
    user_id = settings.DEFAULT_USER_ID
    for w in range(1, 17):
        stmt = select(MilestoneVerification).where(
            MilestoneVerification.user_id == user_id, MilestoneVerification.week_number == w
        )
        existing = (await db.execute(stmt)).scalar_one_or_none()
        if not existing:
            init_status = "in_progress" if w == 1 else "locked"
            m = MilestoneVerification(
                user_id=user_id, week_number=w, status=init_status, evidence_notes=None
            )
            db.add(m)

    # 6. Initialize Core Project Tasks for each week milestone
    for w_data in data["weeks"]:
        w_num = w_data["week_number"]
        task_id = f"task-w{w_num:02d}-milestone"
        linked_day = w_num * 7  # e.g. Day 7 for Week 1, Day 14 for Week 2, etc.

        stmt = select(ProjectTask).where(ProjectTask.user_id == user_id, ProjectTask.id == task_id)
        existing = (await db.execute(stmt)).scalar_one_or_none()
        if not existing:
            pt = ProjectTask(
                id=task_id,
                user_id=user_id,
                phase_number=w_data["phase_number"],
                week_number=w_num,
                linked_day_number=linked_day,
                title=f"Week {w_num} Milestone: {w_data['milestone_title']}",
                description=w_data["milestone_description"],
                implementation_notes=None,
                git_commit_ref=None,
                pr_url=None,
                test_results=None,
                remaining_issues=None,
                status="not_started",
            )
            db.add(pt)

    await db.commit()
    logger.info("Curriculum seeding completed successfully: 112 days ready.")
