from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.models.curriculum import Lesson
from app.models.notes import Bookmark, LearningNote
from app.models.project import LearningActivity
from app.schemas.notes import (
    BookmarkOut,
    BookmarkToggle,
    LearningNoteOut,
    NoteCreateUpdate,
)

router = APIRouter(tags=["Notes & Bookmarks"])


def utc_now() -> datetime:
    return datetime.now(UTC)


@router.get("/notes", response_model=list[LearningNoteOut])
async def list_notes(user_id: str = settings.DEFAULT_USER_ID, db: AsyncSession = Depends(get_db)):
    stmt = (
        select(LearningNote, Lesson.title)
        .join(Lesson, LearningNote.lesson_id == Lesson.id)
        .where(LearningNote.user_id == user_id)
        .order_by(LearningNote.updated_at.desc())
    )
    rows = (await db.execute(stmt)).all()
    return [
        LearningNoteOut(
            id=n.id,
            lesson_id=n.lesson_id,
            day_number=n.day_number,
            title=n.title,
            content=n.content,
            lesson_title=lesson_title,
            created_at=n.created_at,
            updated_at=n.updated_at,
        )
        for n, lesson_title in rows
    ]


@router.post("/notes", response_model=LearningNoteOut)
async def create_or_update_note(
    payload: NoteCreateUpdate,
    user_id: str = settings.DEFAULT_USER_ID,
    db: AsyncSession = Depends(get_db),
):
    lesson_id = payload.lesson_id
    if not lesson_id.startswith("day-") and str(payload.day_number).isdigit():
        lesson_id = f"day-{payload.day_number:03d}"

    stmt = select(LearningNote).where(
        LearningNote.user_id == user_id, LearningNote.lesson_id == lesson_id
    )
    note = (await db.execute(stmt)).scalar_one_or_none()
    now = utc_now()

    if not note:
        note = LearningNote(
            user_id=user_id,
            lesson_id=lesson_id,
            day_number=payload.day_number,
            title=payload.title,
            content=payload.content,
            created_at=now,
            updated_at=now,
        )
        db.add(note)
    else:
        note.title = payload.title
        note.content = payload.content
        note.updated_at = now

    act = LearningActivity(
        user_id=user_id,
        activity_type="note_saved",
        day_number=payload.day_number,
        summary=f"Saved study notes for Day {payload.day_number}",
        metadata_json={"lesson_id": lesson_id},
        created_at=now,
    )
    db.add(act)

    await db.commit()
    await db.refresh(note)

    # Get lesson title
    l_stmt = select(Lesson.title).where(Lesson.id == lesson_id)
    l_title = (await db.execute(l_stmt)).scalar()

    return LearningNoteOut(
        id=note.id,
        lesson_id=note.lesson_id,
        day_number=note.day_number,
        title=note.title,
        content=note.content,
        lesson_title=l_title,
        created_at=note.created_at,
        updated_at=note.updated_at,
    )


@router.delete("/notes/{note_id}")
async def delete_note(
    note_id: int, user_id: str = settings.DEFAULT_USER_ID, db: AsyncSession = Depends(get_db)
):
    stmt = select(LearningNote).where(LearningNote.id == note_id, LearningNote.user_id == user_id)
    note = (await db.execute(stmt)).scalar_one_or_none()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found.")

    await db.delete(note)
    await db.commit()
    return {"message": "Note deleted successfully."}


@router.get("/bookmarks", response_model=list[BookmarkOut])
async def list_bookmarks(
    user_id: str = settings.DEFAULT_USER_ID, db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Bookmark, Lesson.title)
        .join(Lesson, Bookmark.lesson_id == Lesson.id)
        .where(Bookmark.user_id == user_id)
        .order_by(Bookmark.day_number)
    )
    rows = (await db.execute(stmt)).all()
    return [
        BookmarkOut(
            id=b.id,
            lesson_id=b.lesson_id,
            day_number=b.day_number,
            tag=b.tag,
            note=b.note,
            lesson_title=lesson_title,
            created_at=b.created_at,
        )
        for b, lesson_title in rows
    ]


@router.post("/bookmarks/toggle")
async def toggle_bookmark(
    payload: BookmarkToggle,
    user_id: str = settings.DEFAULT_USER_ID,
    db: AsyncSession = Depends(get_db),
):
    lesson_id = payload.lesson_id
    if not lesson_id.startswith("day-") and str(payload.day_number).isdigit():
        lesson_id = f"day-{payload.day_number:03d}"

    stmt = select(Bookmark).where(Bookmark.user_id == user_id, Bookmark.lesson_id == lesson_id)
    existing = (await db.execute(stmt)).scalar_one_or_none()

    if existing:
        await db.delete(existing)
        is_bookmarked = False
    else:
        bm = Bookmark(
            user_id=user_id,
            lesson_id=lesson_id,
            day_number=payload.day_number,
            tag=payload.tag,
            note=payload.note,
            created_at=utc_now(),
        )
        db.add(bm)
        is_bookmarked = True

    await db.commit()
    return {"lesson_id": lesson_id, "is_bookmarked": is_bookmarked}
