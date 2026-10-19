from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.curriculum import Lesson, QuizQuestion
from app.schemas.quiz import PracticeQuestionOut

router = APIRouter(prefix="/practice", tags=["Practice Lab"])


@router.get("/questions", response_model=list[PracticeQuestionOut])
async def get_practice_questions(
    question_type: str | None = Query(
        None, description="Filter by question_type: mcq, code_reading, output_prediction, debugging"
    ),
    week: int | None = Query(None, ge=1, le=16, description="Filter by week number"),
    day: int | None = Query(None, ge=1, le=112, description="Filter by day number"),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    stmt = (
        select(QuizQuestion, Lesson.title)
        .join(Lesson, QuizQuestion.lesson_id == Lesson.id)
        .order_by(QuizQuestion.day_number)
    )

    if question_type:
        stmt = stmt.where(QuizQuestion.question_type == question_type)
    if day:
        stmt = stmt.where(QuizQuestion.day_number == day)
    elif week:
        start_day = (week - 1) * 7 + 1
        end_day = week * 7
        stmt = stmt.where(QuizQuestion.day_number.between(start_day, end_day))

    stmt = stmt.limit(limit)
    rows = (await db.execute(stmt)).all()

    return [
        PracticeQuestionOut(
            id=q.id,
            day_number=q.day_number,
            lesson_title=lesson_title,
            question_text=q.question_text,
            question_type=q.question_type,
            code_snippet=q.code_snippet,
            options=q.options or [],
            explanation=q.explanation,
        )
        for q, lesson_title in rows
    ]
