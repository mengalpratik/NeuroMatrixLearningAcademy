from datetime import UTC, datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


def utc_now() -> datetime:
    return datetime.now(UTC)


class LessonProgress(Base):
    __tablename__ = "lesson_progress"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    lesson_id: Mapped[str] = mapped_column(
        String(50), ForeignKey("lessons.id"), index=True, nullable=False
    )
    day_number: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    status: Mapped[str] = mapped_column(
        String(20), default="not_started", nullable=False
    )  # not_started, in_progress, completed
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_accessed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, onupdate=utc_now
    )


class ExerciseAttempt(Base):
    __tablename__ = "exercise_attempts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    lesson_id: Mapped[str] = mapped_column(
        String(50), ForeignKey("lessons.id"), index=True, nullable=False
    )
    exercise_id: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(
        String(20), default="passed", nullable=False
    )  # attempted, passed, failed
    submitted_output: Mapped[str | None] = mapped_column(Text, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    attempted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    lesson_id: Mapped[str] = mapped_column(
        String(50), ForeignKey("lessons.id"), index=True, nullable=False
    )
    question_id: Mapped[str] = mapped_column(
        String(60), ForeignKey("quiz_questions.id"), index=True, nullable=False
    )
    selected_answer: Mapped[str] = mapped_column(String(200), nullable=False)
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    score: Mapped[int] = mapped_column(Integer, default=1)
    attempted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
