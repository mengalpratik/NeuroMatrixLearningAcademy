from typing import Any

from sqlalchemy import JSON, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class CurriculumPhase(Base):
    __tablename__ = "curriculum_phases"

    phase_number: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    weeks_range: Mapped[str] = mapped_column(String(50), nullable=False)
    days_range: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    focus_area: Mapped[str] = mapped_column(String(100), nullable=False)

    weeks: Mapped[list["CurriculumWeek"]] = relationship(
        "CurriculumWeek", back_populates="phase", cascade="all, delete-orphan"
    )


class CurriculumWeek(Base):
    __tablename__ = "curriculum_weeks"

    week_number: Mapped[int] = mapped_column(Integer, primary_key=True)
    phase_number: Mapped[int] = mapped_column(
        Integer, ForeignKey("curriculum_phases.phase_number"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    days_range: Mapped[str] = mapped_column(String(50), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    milestone_title: Mapped[str] = mapped_column(String(150), nullable=False)
    milestone_description: Mapped[str] = mapped_column(Text, nullable=False)
    milestone_criteria: Mapped[list[str]] = mapped_column(JSON, default=list)

    phase: Mapped["CurriculumPhase"] = relationship("CurriculumPhase", back_populates="weeks")
    lessons: Mapped[list["Lesson"]] = relationship(
        "Lesson", back_populates="week", cascade="all, delete-orphan"
    )


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)  # e.g. "day-001"
    day_number: Mapped[int] = mapped_column(Integer, unique=True, index=True, nullable=False)
    week_number: Mapped[int] = mapped_column(
        Integer, ForeignKey("curriculum_weeks.week_number"), nullable=False
    )
    phase_number: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    slug: Mapped[str] = mapped_column(String(200), index=True, nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, default=60)

    # Structured pedagogical sections
    objectives: Mapped[list[str]] = mapped_column(JSON, default=list)
    prerequisites: Mapped[list[str]] = mapped_column(JSON, default=list)
    revision_questions: Mapped[list[str]] = mapped_column(JSON, default=list)
    concept_sections: Mapped[list[dict[str, Any]]] = mapped_column(JSON, default=list)
    code_examples: Mapped[list[dict[str, Any]]] = mapped_column(JSON, default=list)
    exercises: Mapped[list[dict[str, Any]]] = mapped_column(JSON, default=list)
    common_errors: Mapped[list[dict[str, Any]]] = mapped_column(JSON, default=list)
    edge_cases: Mapped[list[str]] = mapped_column(JSON, default=list)
    neuromatrix_integration: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    completion_criteria: Mapped[list[str]] = mapped_column(JSON, default=list)

    week: Mapped["CurriculumWeek"] = relationship("CurriculumWeek", back_populates="lessons")
    quizzes: Mapped[list["QuizQuestion"]] = relationship(
        "QuizQuestion", back_populates="lesson", cascade="all, delete-orphan"
    )


class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id: Mapped[str] = mapped_column(String(60), primary_key=True)  # e.g. "quiz-d1-q1"
    lesson_id: Mapped[str] = mapped_column(
        String(50), ForeignKey("lessons.id"), index=True, nullable=False
    )
    day_number: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    question_text: Mapped[str] = mapped_column(Text, nullable=False)
    question_type: Mapped[str] = mapped_column(
        String(50), default="mcq"
    )  # mcq, code_reading, output_prediction, debugging
    code_snippet: Mapped[str | None] = mapped_column(Text, nullable=True)
    options: Mapped[list[str]] = mapped_column(JSON, default=list)
    correct_answer: Mapped[str] = mapped_column(String(200), nullable=False)
    explanation: Mapped[str] = mapped_column(Text, nullable=False)

    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="quizzes")
