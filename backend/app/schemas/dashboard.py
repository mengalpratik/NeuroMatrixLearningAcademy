from pydantic import BaseModel

from app.schemas.project import LearningActivityOut, MilestoneVerificationOut


class DashboardTodayLesson(BaseModel):
    id: str
    day_number: int
    week_number: int
    phase_number: int
    title: str
    summary: str
    duration_minutes: int
    status: str


class DashboardSummaryOut(BaseModel):
    current_day: int
    current_week: int
    current_phase: int
    total_days: int = 112
    completed_days: int
    in_progress_days: int
    remaining_days: int
    completion_percentage: float
    today_lesson: DashboardTodayLesson | None
    weekly_milestones: list[MilestoneVerificationOut]
    recent_activities: list[LearningActivityOut]
    bookmarked_count: int
    notes_count: int
