from pydantic import BaseModel, Field


class ConceptSection(BaseModel):
    title: str
    content: str
    key_points: list[str] = Field(default_factory=list)


class CodeExample(BaseModel):
    title: str
    description: str
    code: str
    language: str = "python"
    expected_output: str


class Exercise(BaseModel):
    id: str
    title: str
    difficulty: str = "beginner"  # beginner, intermediate, advanced
    instructions: str
    starter_code: str
    solution_code: str
    expected_output: str
    acceptance_criteria: list[str] = Field(default_factory=list)
    test_cases: list[str] = Field(default_factory=list)


class CommonError(BaseModel):
    error_type: str
    cause: str
    fix: str
    example: str = ""


class NeuroMatrixIntegration(BaseModel):
    topic: str
    context: str
    task_description: str
    target_component: str
    verification_step: str


class QuizQuestionOut(BaseModel):
    id: str
    day_number: int
    question_text: str
    question_type: str
    code_snippet: str | None = None
    options: list[str]
    explanation: str


class LessonSummaryOut(BaseModel):
    id: str
    day_number: int
    week_number: int
    phase_number: int
    title: str
    slug: str
    summary: str
    duration_minutes: int
    status: str = "not_started"
    is_bookmarked: bool = False
    has_notes: bool = False


class LessonDetailOut(BaseModel):
    id: str
    day_number: int
    week_number: int
    phase_number: int
    title: str
    slug: str
    summary: str
    duration_minutes: int
    objectives: list[str]
    prerequisites: list[str]
    revision_questions: list[str]
    concept_sections: list[ConceptSection]
    code_examples: list[CodeExample]
    exercises: list[Exercise]
    common_errors: list[CommonError]
    edge_cases: list[str]
    neuromatrix_integration: NeuroMatrixIntegration
    completion_criteria: list[str]
    quizzes: list[QuizQuestionOut]
    status: str = "not_started"
    is_bookmarked: bool = False
    current_note: str | None = None
    prev_day: int | None = None
    next_day: int | None = None


class WeekOverviewOut(BaseModel):
    week_number: int
    phase_number: int
    title: str
    days_range: str
    summary: str
    milestone_title: str
    milestone_description: str
    milestone_criteria: list[str]
    milestone_status: str = "locked"  # locked, in_progress, ready_for_review, verified
    lessons: list[LessonSummaryOut]


class PhaseOverviewOut(BaseModel):
    phase_number: int
    title: str
    weeks_range: str
    days_range: str
    description: str
    focus_area: str
    weeks: list[WeekOverviewOut]


class CurriculumOverviewOut(BaseModel):
    phases: list[PhaseOverviewOut]
    total_days: int = 112
    completed_days: int = 0
    in_progress_days: int = 0
