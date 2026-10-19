import {
  BookmarkOut,
  CurriculumOverviewOut,
  DashboardSummaryOut,
  ExerciseAttemptOut,
  LearningNoteOut,
  LessonDetailOut,
  LessonSummaryOut,
  MilestoneVerificationOut,
  PracticeQuestionOut,
  ProjectTaskOut,
  ProjectTaskUpdate,
  QuizAnswerSubmit,
  QuizBatchResult,
} from './types';

const BASE_URL = '/api';

async function request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const url = `${BASE_URL}${endpoint}`;
  const headers: HeadersInit = {
    'Content-Type': 'application/json',
    ...(options.headers || {}),
  };

  const response = await fetch(url, {
    ...options,
    headers,
  });

  if (!response.ok) {
    let errorDetail = `HTTP ${response.status} ${response.statusText}`;
    try {
      const errJson = await response.json();
      if (errJson.detail) {
        errorDetail = typeof errJson.detail === 'string' ? errJson.detail : JSON.stringify(errJson.detail);
      }
    } catch {
      // ignore json parse error
    }
    throw new Error(errorDetail);
  }

  return response.json();
}

export const api = {
  // Health
  checkHealth: () => request<{ status: string; database: string }>('/health'),

  // Dashboard
  getDashboardSummary: () => request<DashboardSummaryOut>('/dashboard/summary'),

  // Curriculum
  getCurriculumOverview: () => request<CurriculumOverviewOut>('/curriculum/overview'),

  searchLessons: (query?: string, phase?: number, status?: string, topic?: string) => {
    const params = new URLSearchParams();
    if (query) params.append('q', query);
    if (phase) params.append('phase', phase.toString());
    if (status) params.append('status', status);
    if (topic) params.append('topic', topic);
    const qs = params.toString();
    return request<LessonSummaryOut[]>(`/curriculum/search${qs ? `?${qs}` : ''}`);
  },

  getLesson: (dayOrId: string | number) => request<LessonDetailOut>(`/lessons/${dayOrId}`),

  // Progress
  updateLessonStatus: (dayOrId: string | number, status: 'not_started' | 'in_progress' | 'completed') =>
    request<{ status: string; day_number: number }>(`/lessons/${dayOrId}/status`, {
      method: 'POST',
      body: JSON.stringify({ status }),
    }),

  // Exercises
  submitExercise: (dayOrId: string | number, exerciseId: string, submitted_output: string, notes?: string) =>
    request<ExerciseAttemptOut>(`/lessons/${dayOrId}/exercises/${exerciseId}/submit`, {
      method: 'POST',
      body: JSON.stringify({ submitted_output, notes }),
    }),

  // Quiz
  submitQuiz: (dayOrId: string | number, answers: QuizAnswerSubmit[]) =>
    request<QuizBatchResult>(`/lessons/${dayOrId}/quiz/submit`, {
      method: 'POST',
      body: JSON.stringify({ answers }),
    }),

  // Practice
  getPracticeQuestions: (questionType?: string, week?: number, day?: number, limit = 20) => {
    const params = new URLSearchParams();
    if (questionType) params.append('question_type', questionType);
    if (week) params.append('week', week.toString());
    if (day) params.append('day', day.toString());
    params.append('limit', limit.toString());
    return request<PracticeQuestionOut[]>(`/practice/questions?${params.toString()}`);
  },

  // Projects & Milestones
  getProjectTasks: () => request<ProjectTaskOut[]>('/projects'),

  updateProjectTask: (taskId: string, payload: ProjectTaskUpdate) =>
    request<ProjectTaskOut>(`/projects/${taskId}`, {
      method: 'PATCH',
      body: JSON.stringify(payload),
    }),

  verifyMilestone: (weekNumber: number, evidenceNotes: string, status: string = 'ready_for_review') =>
    request<MilestoneVerificationOut>(`/milestones/${weekNumber}/verify`, {
      method: 'POST',
      body: JSON.stringify({ evidence_notes: evidenceNotes, status }),
    }),

  // Notes & Bookmarks
  getNotes: () => request<LearningNoteOut[]>('/notes'),

  saveNote: (dayNumber: number, title: string, content: string) =>
    request<LearningNoteOut>('/notes', {
      method: 'POST',
      body: JSON.stringify({
        lesson_id: `day-${String(dayNumber).padStart(3, '0')}`,
        day_number: dayNumber,
        title,
        content,
      }),
    }),

  deleteNote: (id: number) =>
    request<{ message: string }>(`/notes/${id}`, {
      method: 'DELETE',
    }),

  getBookmarks: () => request<BookmarkOut[]>('/bookmarks'),

  toggleBookmark: (dayNumber: number, tag?: string, note?: string) =>
    request<{ lesson_id: string; is_bookmarked: boolean }>('/bookmarks/toggle', {
      method: 'POST',
      body: JSON.stringify({
        lesson_id: `day-${String(dayNumber).padStart(3, '0')}`,
        day_number: dayNumber,
        tag,
        note,
      }),
    }),
};
