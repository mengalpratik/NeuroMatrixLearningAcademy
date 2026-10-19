from datetime import UTC, datetime
from typing import Any

from sqlalchemy import JSON, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


def utc_now() -> datetime:
    return datetime.now(UTC)


class ProjectTask(Base):
    __tablename__ = "project_tasks"

    id: Mapped[str] = mapped_column(String(60), primary_key=True)  # e.g. "task-w01-cli"
    user_id: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    phase_number: Mapped[int] = mapped_column(Integer, nullable=False)
    week_number: Mapped[int] = mapped_column(Integer, nullable=False)
    linked_day_number: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    implementation_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    git_commit_ref: Mapped[str | None] = mapped_column(String(100), nullable=True)
    pr_url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    test_results: Mapped[str | None] = mapped_column(Text, nullable=True)
    remaining_issues: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        String(30), default="not_started", nullable=False
    )  # not_started, in_progress, completed, verified
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, onupdate=utc_now
    )


class MilestoneVerification(Base):
    __tablename__ = "milestone_verifications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    week_number: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    status: Mapped[str] = mapped_column(
        String(30), default="locked", nullable=False
    )  # locked, in_progress, ready_for_review, verified
    evidence_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    verified_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class LearningActivity(Base):
    __tablename__ = "learning_activities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    activity_type: Mapped[str] = mapped_column(String(50), nullable=False)
    day_number: Mapped[int | None] = mapped_column(Integer, nullable=True)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    metadata_json: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
