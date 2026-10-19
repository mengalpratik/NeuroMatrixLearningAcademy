from datetime import datetime

from pydantic import BaseModel, Field


class LessonStatusUpdate(BaseModel):
    status: str = Field(..., pattern="^(not_started|in_progress|completed)$")


class LessonProgressOut(BaseModel):
    lesson_id: str
    day_number: int
    status: str
    started_at: datetime | None = None
    completed_at: datetime | None = None
    last_accessed_at: datetime


class ExerciseSubmission(BaseModel):
    submitted_output: str
    notes: str | None = None


class ExerciseAttemptOut(BaseModel):
    id: int
    lesson_id: str
    exercise_id: str
    status: str
    submitted_output: str | None
    notes: str | None
    attempted_at: datetime
