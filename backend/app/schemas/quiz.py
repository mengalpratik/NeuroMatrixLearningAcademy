from pydantic import BaseModel


class QuizAnswerSubmit(BaseModel):
    question_id: str
    selected_answer: str


class QuizAnswerResult(BaseModel):
    question_id: str
    selected_answer: str
    correct_answer: str
    is_correct: bool
    explanation: str


class QuizSubmissionBatch(BaseModel):
    answers: list[QuizAnswerSubmit]


class QuizBatchResult(BaseModel):
    lesson_id: str
    day_number: int
    total_questions: int
    correct_count: int
    score_percentage: float
    results: list[QuizAnswerResult]


class PracticeQuestionOut(BaseModel):
    id: str
    day_number: int
    lesson_title: str
    question_text: str
    question_type: str
    code_snippet: str | None = None
    options: list[str]
    explanation: str
