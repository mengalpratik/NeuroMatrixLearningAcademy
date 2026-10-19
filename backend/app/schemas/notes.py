from datetime import datetime

from pydantic import BaseModel


class BookmarkToggle(BaseModel):
    lesson_id: str
    day_number: int
    tag: str | None = None
    note: str | None = None


class BookmarkOut(BaseModel):
    id: int
    lesson_id: str
    day_number: int
    tag: str | None
    note: str | None
    lesson_title: str | None = None
    created_at: datetime


class NoteCreateUpdate(BaseModel):
    lesson_id: str
    day_number: int
    title: str
    content: str


class LearningNoteOut(BaseModel):
    id: int
    lesson_id: str
    day_number: int
    title: str
    content: str
    lesson_title: str | None = None
    created_at: datetime
    updated_at: datetime
