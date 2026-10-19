from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.schemas.progress import LessonProgressOut, LessonStatusUpdate
from app.services.progress_service import update_lesson_status

router = APIRouter(tags=["Progress"])


@router.post("/lessons/{day_or_id}/status", response_model=LessonProgressOut)
async def set_status(
    day_or_id: str,
    payload: LessonStatusUpdate,
    user_id: str = settings.DEFAULT_USER_ID,
    db: AsyncSession = Depends(get_db),
):
    try:
        prog = await update_lesson_status(
            db=db, user_id=user_id, day_or_id=day_or_id, new_status=payload.status
        )
        return LessonProgressOut(
            lesson_id=prog.lesson_id,
            day_number=prog.day_number,
            status=prog.status,
            started_at=prog.started_at,
            completed_at=prog.completed_at,
            last_accessed_at=prog.last_accessed_at,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
