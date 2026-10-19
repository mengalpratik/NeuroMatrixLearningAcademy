from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.schemas.quiz import QuizBatchResult, QuizSubmissionBatch
from app.services.progress_service import evaluate_quiz_answers

router = APIRouter(tags=["Quiz"])


@router.post("/lessons/{day_or_id}/quiz/submit", response_model=QuizBatchResult)
async def submit_quiz(
    day_or_id: str,
    payload: QuizSubmissionBatch,
    user_id: str = settings.DEFAULT_USER_ID,
    db: AsyncSession = Depends(get_db),
):
    lesson_id = f"day-{int(day_or_id):03d}" if day_or_id.isdigit() else day_or_id
    if not payload.answers:
        raise HTTPException(
            status_code=400, detail="No quiz answers provided in submission payload."
        )

    return await evaluate_quiz_answers(
        db=db, user_id=user_id, lesson_id=lesson_id, answers=payload.answers
    )
