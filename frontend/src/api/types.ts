export interface ConceptSection {
  title: string;
  content: string;
  key_points: string[];
}

export interface CodeExample {
  title: string;
  description: string;
  code: string;
  language: string;
  expected_output: string;
}

export interface Exercise {
  id: string;
  title: string;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  instructions: string;
  starter_code: string;
  solution_code: string;
  expected_output: string;
  acceptance_criteria: string[];
  test_cases: string[];
}

export interface CommonError {
  error_type: string;
  cause: string;
  fix: string;
  example: string;
}

export interface NeuroMatrixIntegration {
  topic: string;
  context: string;
  task_description: string;
  target_component: string;
  verification_step: string;
}

export interface QuizQuestionOut {
  id: string;
  day_number: number;
  question_text: string;
  question_type: string;
  code_snippet: string | null;
  options: string[];
  explanation: string;
}

export interface LessonSummaryOut {
  id: string;
  day_number: number;
  week_number: number;
  phase_number: number;
  title: string;
  slug: string;
  summary: string;
  duration_minutes: number;
  status: 'not_started' | 'in_progress' | 'completed';
  is_bookmarked: boolean;
  has_notes: boolean;
}

export interface LessonDetailOut {
  id: string;
  day_number: number;
  week_number: number;
  phase_number: number;
  title: string;
  slug: string;
  summary: string;
  duration_minutes: number;
  objectives: string[];
  prerequisites: string[];
  revision_questions: string[];
  concept_sections: ConceptSection[];
  code_examples: CodeExample[];
  exercises: Exercise[];
  common_errors: CommonError[];
  edge_cases: string[];
  neuromatrix_integration: NeuroMatrixIntegration;
  completion_criteria: string[];
  quizzes: QuizQuestionOut[];
  status: 'not_started' | 'in_progress' | 'completed';
  is_bookmarked: boolean;
  current_note: string | null;
  prev_day: number | null;
  next_day: number | null;
}

export interface WeekOverviewOut {
  week_number: number;
  phase_number: number;
  title: string;
  days_range: string;
  summary: string;
  milestone_title: string;
  milestone_description: string;
  milestone_criteria: string[];
  milestone_status: 'locked' | 'in_progress' | 'ready_for_review' | 'verified';
  lessons: LessonSummaryOut[];
}

export interface PhaseOverviewOut {
  phase_number: number;
  title: string;
  weeks_range: string;
  days_range: string;
  description: string;
  focus_area: string;
  weeks: WeekOverviewOut[];
}

export interface CurriculumOverviewOut {
  phases: PhaseOverviewOut[];
  total_days: number;
  completed_days: number;
  in_progress_days: number;
}

export interface DashboardTodayLesson {
  id: string;
  day_number: number;
  week_number: number;
  phase_number: number;
  title: string;
  summary: string;
  duration_minutes: number;
  status: 'not_started' | 'in_progress' | 'completed';
}

export interface MilestoneVerificationOut {
  week_number: number;
  status: string;
  evidence_notes: string | null;
  verified_at: string | null;
}

export interface LearningActivityOut {
  id: number;
  activity_type: string;
  day_number: number | null;
  summary: string;
  created_at: string;
}

export interface DashboardSummaryOut {
  current_day: number;
  current_week: number;
  current_phase: number;
  total_days: number;
  completed_days: number;
  in_progress_days: number;
  remaining_days: number;
  completion_percentage: number;
  today_lesson: DashboardTodayLesson | null;
  weekly_milestones: MilestoneVerificationOut[];
  recent_activities: LearningActivityOut[];
  bookmarked_count: number;
  notes_count: number;
}

export interface ExerciseAttemptOut {
  id: number;
  lesson_id: string;
  exercise_id: string;
  status: string;
  submitted_output: string | null;
  notes: string | null;
  attempted_at: string;
}

export interface QuizAnswerSubmit {
  question_id: string;
  selected_answer: string;
}

export interface QuizAnswerResult {
  question_id: string;
  selected_answer: string;
  correct_answer: string;
  is_correct: boolean;
  explanation: string;
}

export interface QuizBatchResult {
  lesson_id: string;
  day_number: number;
  total_questions: number;
  correct_count: number;
  score_percentage: number;
  results: QuizAnswerResult[];
}

export interface PracticeQuestionOut {
  id: string;
  day_number: number;
  lesson_title: string;
  question_text: string;
  question_type: string;
  code_snippet: string | null;
  options: string[];
  explanation: string;
}

export interface ProjectTaskOut {
  id: string;
  phase_number: number;
  week_number: number;
  linked_day_number: number;
  title: string;
  description: string;
  implementation_notes: string | null;
  git_commit_ref: string | null;
  pr_url: string | null;
  test_results: string | null;
  remaining_issues: string | null;
  status: 'not_started' | 'in_progress' | 'completed' | 'verified';
  created_at: string;
  updated_at: string;
}

export interface ProjectTaskUpdate {
  status: 'not_started' | 'in_progress' | 'completed' | 'verified';
  implementation_notes?: string;
  git_commit_ref?: string;
  pr_url?: string;
  test_results?: string;
  remaining_issues?: string;
}

export interface LearningNoteOut {
  id: number;
  lesson_id: string;
  day_number: number;
  title: string;
  content: string;
  lesson_title?: string;
  created_at: string;
  updated_at: string;
}

export interface BookmarkOut {
  id: number;
  lesson_id: string;
  day_number: number;
  tag: string | null;
  note: string | null;
  lesson_title?: string;
  created_at: string;
}
