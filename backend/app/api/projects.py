from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.models.project import LearningActivity, MilestoneVerification, ProjectTask
from app.schemas.project import (
    MilestoneVerificationOut,
    MilestoneVerificationSubmit,
    ProjectTaskOut,
    ProjectTaskUpdate,
)

router = APIRouter(tags=["Project Lab & Milestones"])


def utc_now() -> datetime:
    return datetime.now(UTC)


@router.get("/projects", response_model=list[ProjectTaskOut])
async def list_project_tasks(
    user_id: str = settings.DEFAULT_USER_ID, db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(ProjectTask).where(ProjectTask.user_id == user_id).order_by(ProjectTask.week_number)
    )
    tasks = (await db.execute(stmt)).scalars().all()
    return [
        ProjectTaskOut(
            id=t.id,
            phase_number=t.phase_number,
            week_number=t.week_number,
            linked_day_number=t.linked_day_number,
            title=t.title,
            description=t.description,
            implementation_notes=t.implementation_notes,
            git_commit_ref=t.git_commit_ref,
            pr_url=t.pr_url,
            test_results=t.test_results,
            remaining_issues=t.remaining_issues,
            status=t.status,
            created_at=t.created_at,
            updated_at=t.updated_at,
        )
        for t in tasks
    ]


@router.patch("/projects/{task_id}", response_model=ProjectTaskOut)
async def update_project_task(
    task_id: str,
    payload: ProjectTaskUpdate,
    user_id: str = settings.DEFAULT_USER_ID,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(ProjectTask).where(ProjectTask.id == task_id, ProjectTask.user_id == user_id)
    task = (await db.execute(stmt)).scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail=f"Project task '{task_id}' not found.")

    task.status = payload.status
    if payload.implementation_notes is not None:
        task.implementation_notes = payload.implementation_notes
    if payload.git_commit_ref is not None:
        task.git_commit_ref = payload.git_commit_ref
    if payload.pr_url is not None:
        task.pr_url = payload.pr_url
    if payload.test_results is not None:
        task.test_results = payload.test_results
    if payload.remaining_issues is not None:
        task.remaining_issues = payload.remaining_issues
    task.updated_at = utc_now()

    # Log activity
    act = LearningActivity(
        user_id=user_id,
        activity_type="project_task_updated",
        day_number=task.linked_day_number,
        summary=f"Updated {task.title} to '{task.status}'",
        metadata_json={"task_id": task.id, "status": task.status},
        created_at=utc_now(),
    )
    db.add(act)

    await db.commit()
    await db.refresh(task)

    return ProjectTaskOut(
        id=task.id,
        phase_number=task.phase_number,
        week_number=task.week_number,
        linked_day_number=task.linked_day_number,
        title=task.title,
        description=task.description,
        implementation_notes=task.implementation_notes,
        git_commit_ref=task.git_commit_ref,
        pr_url=task.pr_url,
        test_results=task.test_results,
        remaining_issues=task.remaining_issues,
        status=task.status,
        created_at=task.created_at,
        updated_at=task.updated_at,
    )


@router.post("/milestones/{week_number}/verify", response_model=MilestoneVerificationOut)
async def verify_milestone(
    week_number: int,
    payload: MilestoneVerificationSubmit,
    user_id: str = settings.DEFAULT_USER_ID,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(MilestoneVerification).where(
        MilestoneVerification.user_id == user_id, MilestoneVerification.week_number == week_number
    )
    m = (await db.execute(stmt)).scalar_one_or_none()
    now = utc_now()
    if not m:
        m = MilestoneVerification(
            user_id=user_id,
            week_number=week_number,
            status=payload.status,
            evidence_notes=payload.evidence_notes,
            verified_at=now if payload.status == "verified" else None,
        )
        db.add(m)
    else:
        m.status = payload.status
        m.evidence_notes = payload.evidence_notes
        if payload.status == "verified" and not m.verified_at:
            m.verified_at = now

    act = LearningActivity(
        user_id=user_id,
        activity_type="milestone_verified",
        day_number=week_number * 7,
        summary=f"Updated Week {week_number} Milestone verification status to '{payload.status}'",
        metadata_json={"week_number": week_number, "status": payload.status},
        created_at=now,
    )
    db.add(act)

    await db.commit()
    await db.refresh(m)

    return MilestoneVerificationOut(
        week_number=m.week_number,
        status=m.status,
        evidence_notes=m.evidence_notes,
        verified_at=m.verified_at,
    )
