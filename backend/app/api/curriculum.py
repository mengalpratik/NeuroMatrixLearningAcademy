from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.schemas.curriculum import (
    CurriculumOverviewOut,
    LessonDetailOut,
    LessonSummaryOut,
)
from app.services.curriculum_service import (
    get_curriculum_overview,
    get_lesson_by_day_or_id,
    search_lessons,
)

router = APIRouter(tags=["Curriculum"])


@router.get("/curriculum/overview", response_model=CurriculumOverviewOut)
async def get_overview(user_id: str = settings.DEFAULT_USER_ID, db: AsyncSession = Depends(get_db)):
    return await get_curriculum_overview(db=db, user_id=user_id)


@router.get("/curriculum/search", response_model=list[LessonSummaryOut])
async def search(
    q: str | None = Query(None, description="Search query across titles, slugs, and summaries"),
    phase: int | None = Query(None, ge=1, le=4, description="Filter by phase number (1-4)"),
    status: str | None = Query(
        None, description="Filter by status: all, not_started, in_progress, completed"
    ),
    topic: str | None = Query(None, description="Filter by topic keyword"),
    user_id: str = settings.DEFAULT_USER_ID,
    db: AsyncSession = Depends(get_db),
):
    return await search_lessons(
        db=db, user_id=user_id, query=q, phase=phase, status_filter=status, topic=topic
    )


@router.get("/lessons/{day_or_id}", response_model=LessonDetailOut)
async def get_lesson(
    day_or_id: str, user_id: str = settings.DEFAULT_USER_ID, db: AsyncSession = Depends(get_db)
):
    lesson = await get_lesson_by_day_or_id(db=db, user_id=user_id, identifier=day_or_id)
    if not lesson:
        raise HTTPException(status_code=404, detail=f"Lesson '{day_or_id}' not found.")
    return lesson
