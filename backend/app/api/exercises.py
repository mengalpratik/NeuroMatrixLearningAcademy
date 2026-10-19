from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.schemas.progress import ExerciseAttemptOut, ExerciseSubmission
from app.services.progress_service import submit_exercise_attempt

router = APIRouter(tags=["Exercises"])


@router.post(
    "/lessons/{day_or_id}/exercises/{exercise_id}/submit", response_model=ExerciseAttemptOut
)
async def submit_exercise(
    day_or_id: str,
    exercise_id: str,
    payload: ExerciseSubmission,
    user_id: str = settings.DEFAULT_USER_ID,
    db: AsyncSession = Depends(get_db),
):
    lesson_id = f"day-{int(day_or_id):03d}" if day_or_id.isdigit() else day_or_id
    attempt = await submit_exercise_attempt(
        db=db,
        user_id=user_id,
        lesson_id=lesson_id,
        exercise_id=exercise_id,
        submitted_output=payload.submitted_output,
        notes=payload.notes,
    )
    return ExerciseAttemptOut(
        id=attempt.id,
        lesson_id=attempt.lesson_id,
        exercise_id=attempt.exercise_id,
        status=attempt.status,
        submitted_output=attempt.submitted_output,
        notes=attempt.notes,
        attempted_at=attempt.attempted_at,
    )
