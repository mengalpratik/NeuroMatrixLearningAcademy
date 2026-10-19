from datetime import datetime

from pydantic import BaseModel, Field


class ProjectTaskUpdate(BaseModel):
    status: str = Field(..., pattern="^(not_started|in_progress|completed|verified)$")
    implementation_notes: str | None = None
    git_commit_ref: str | None = None
    pr_url: str | None = None
    test_results: str | None = None
    remaining_issues: str | None = None


class ProjectTaskOut(BaseModel):
    id: str
    phase_number: int
    week_number: int
    linked_day_number: int
    title: str
    description: str
    implementation_notes: str | None
    git_commit_ref: str | None
    pr_url: str | None
    test_results: str | None
    remaining_issues: str | None
    status: str
    created_at: datetime
    updated_at: datetime


class MilestoneVerificationSubmit(BaseModel):
    evidence_notes: str
    status: str = Field(
        default="ready_for_review", pattern="^(in_progress|ready_for_review|verified)$"
    )


class MilestoneVerificationOut(BaseModel):
    week_number: int
    status: str
    evidence_notes: str | None
    verified_at: datetime | None


class LearningActivityOut(BaseModel):
    id: int
    activity_type: str
    day_number: int | None
    summary: str
    created_at: datetime
