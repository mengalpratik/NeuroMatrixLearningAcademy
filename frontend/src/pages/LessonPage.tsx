import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import {
  BookOpen,
  CheckCircle2,
  Clock,
  Bookmark,
  ChevronLeft,
  ChevronRight,
  Code,
  AlertTriangle,
  HelpCircle,
  Shield,
  FileText,
  Copy,
  Check,
  Send,
  Eye,
  EyeOff,
  RotateCcw,
} from 'lucide-react';
import { api } from '../api/client';
import { LessonDetailOut, QuizBatchResult } from '../api/types';

export const LessonPage: React.FC = () => {
  const { day } = useParams<{ day: string }>();

  const [lesson, setLesson] = useState<LessonDetailOut | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Active section tab
  const [activeTab, setActiveTab] = useState<
    'concepts' | 'code' | 'exercises' | 'debugging' | 'quiz' | 'neuromatrix' | 'notes'
  >('concepts');

  // Exercise state
  const [submittedOutputs, setSubmittedOutputs] = useState<Record<string, string>>({});
  const [exerciseNotes, setExerciseNotes] = useState<Record<string, string>>({});
  const [exerciseStatus, setExerciseStatus] = useState<Record<string, string>>({});
  const [showSolutions, setShowSolutions] = useState<Record<string, boolean>>({});

  // Quiz state
  const [quizSelections, setQuizSelections] = useState<Record<string, string>>({});
  const [quizResult, setQuizResult] = useState<QuizBatchResult | null>(null);
  const [quizSubmitting, setQuizSubmitting] = useState(false);

  // Note state
  const [noteContent, setNoteContent] = useState('');
  const [noteSaving, setNoteSaving] = useState(false);
  const [noteSaved, setNoteSaved] = useState(false);

  // Copy feedback
  const [copiedCodeId, setCopiedCodeId] = useState<string | null>(null);

  const fetchLesson = (dayIdentifier: string) => {
    setLoading(true);
    setError(null);
    setQuizResult(null);
    api.getLesson(dayIdentifier)
      .then((data) => {
        setLesson(data);
        setNoteContent(data.current_note || '');
      })
      .catch((err) => {
        setError(err.message);
      })
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    if (day) {
      fetchLesson(day);
    }
  }, [day]);

  const handleStatusChange = async (newStatus: 'not_started' | 'in_progress' | 'completed') => {
    if (!lesson) return;
    try {
      await api.updateLessonStatus(lesson.day_number, newStatus);
      setLesson((prev) => (prev ? { ...prev, status: newStatus } : null));
    } catch (err: any) {
      alert(`Error updating status: ${err.message}`);
    }
  };

  const handleToggleBookmark = async () => {
    if (!lesson) return;
    try {
      const res = await api.toggleBookmark(lesson.day_number);
      setLesson((prev) => (prev ? { ...prev, is_bookmarked: res.is_bookmarked } : null));
    } catch (err: any) {
      console.error(err);
    }
  };

  const handleCopy = (text: string, id: string) => {
    navigator.clipboard.writeText(text);
    setCopiedCodeId(id);
    setTimeout(() => setCopiedCodeId(null), 2000);
  };

  const handleExerciseSubmit = async (exerciseId: string) => {
    if (!lesson) return;
    const output = submittedOutputs[exerciseId] || '';
    const notes = exerciseNotes[exerciseId] || '';
    try {
      await api.submitExercise(lesson.day_number, exerciseId, output, notes);
      setExerciseStatus((prev) => ({ ...prev, [exerciseId]: 'passed' }));
    } catch (err: any) {
      alert(`Submission failed: ${err.message}`);
    }
  };

  const handleQuizSubmit = async () => {
    if (!lesson || !lesson.quizzes.length) return;
    const answers = Object.entries(quizSelections).map(([qId, answer]) => ({
      question_id: qId,
      selected_answer: answer,
    }));

    if (answers.length < lesson.quizzes.length) {
      alert('Please answer all questions before submitting the quiz.');
      return;
    }

    setQuizSubmitting(true);
    try {
      const result = await api.submitQuiz(lesson.day_number, answers);
      setQuizResult(result);
    } catch (err: any) {
      alert(`Quiz evaluation error: ${err.message}`);
    } finally {
      setQuizSubmitting(false);
    }
  };

  const handleSaveNote = async () => {
    if (!lesson) return;
    setNoteSaving(true);
    try {
      await api.saveNote(lesson.day_number, `Day ${lesson.day_number} Notes`, noteContent);
      setNoteSaved(true);
      setTimeout(() => setNoteSaved(false), 2500);
    } catch (err: any) {
      alert(`Note save error: ${err.message}`);
    } finally {
      setNoteSaving(false);
    }
  };

  if (loading) {
    return (
      <div className="max-w-5xl mx-auto px-4 py-16 flex flex-col items-center justify-center min-h-[50vh]">
        <div className="w-8 h-8 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mb-4" />
        <span className="font-mono text-sm text-dark-400">Loading Day {day} workspace...</span>
      </div>
    );
  }

  if (error || !lesson) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-16 text-center space-y-4">
        <div className="p-6 rounded-xl bg-red-950/20 border border-red-500/30">
          <h3 className="text-red-400 font-semibold mb-2">Lesson Not Found</h3>
          <p className="text-xs text-dark-300 font-mono mb-4">{error || 'Day does not exist.'}</p>
          <Link
            to="/curriculum"
            className="px-4 py-2 bg-dark-800 hover:bg-dark-700 text-xs font-mono rounded text-dark-200 inline-block"
          >
            Back to Curriculum
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">
      {/* Top Header & Breadcrumb Navigation */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-dark-700 pb-5">
        <div className="space-y-2">
          <div className="flex items-center gap-2">
            <Link
              to="/curriculum"
              className="text-xs font-mono text-dark-400 hover:text-emerald-400 flex items-center gap-1 transition-colors"
            >
              <ChevronLeft className="w-3.5 h-3.5" />
              <span>Curriculum</span>
            </Link>
            <span className="text-dark-600">/</span>
            <span className="px-2 py-0.5 text-[10px] font-mono rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
              Week {lesson.week_number} • Day {lesson.day_number}
            </span>
            <span className="text-xs font-mono text-dark-500">
              {lesson.duration_minutes} mins
            </span>
          </div>

          <h1 className="text-xl sm:text-2xl font-bold tracking-tight text-dark-100">
            Day {lesson.day_number}: {lesson.title}
          </h1>
        </div>

        {/* Action Controls: Bookmark & Status Transition */}
        <div className="flex items-center gap-3 shrink-0">
          <button
            onClick={handleToggleBookmark}
            className={`p-2 rounded-lg border transition-all ${
              lesson.is_bookmarked
                ? 'bg-amber-500/10 border-amber-500/30 text-amber-400'
                : 'bg-dark-900 border-dark-700 text-dark-400 hover:text-dark-200 hover:border-dark-600'
            }`}
            title={lesson.is_bookmarked ? 'Remove Bookmark' : 'Bookmark this day'}
          >
            <Bookmark className={`w-4 h-4 ${lesson.is_bookmarked ? 'fill-current' : ''}`} />
          </button>

          {/* Status Dropdown/Selector */}
          <div className="flex items-center rounded-lg bg-dark-900 border border-dark-700 p-0.5 text-xs font-mono">
            <button
              onClick={() => handleStatusChange('not_started')}
              className={`px-2.5 py-1.5 rounded transition-all ${
                lesson.status === 'not_started'
                  ? 'bg-dark-800 text-dark-200 font-semibold'
                  : 'text-dark-500 hover:text-dark-300'
              }`}
            >
              Reset
            </button>
            <button
              onClick={() => handleStatusChange('in_progress')}
              className={`px-2.5 py-1.5 rounded transition-all flex items-center gap-1 ${
                lesson.status === 'in_progress'
                  ? 'bg-amber-500/20 text-amber-300 font-semibold'
                  : 'text-dark-500 hover:text-dark-300'
              }`}
            >
              <Clock className="w-3 h-3" /> In Progress
            </button>
            <button
              onClick={() => handleStatusChange('completed')}
              className={`px-2.5 py-1.5 rounded transition-all flex items-center gap-1 ${
                lesson.status === 'completed'
                  ? 'bg-emerald-500/20 text-emerald-400 font-semibold'
                  : 'text-dark-500 hover:text-dark-300'
              }`}
            >
              <CheckCircle2 className="w-3 h-3" /> Complete
            </button>
          </div>
        </div>
      </div>

      {/* Prerequisites & Objectives Callout */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Learning Objectives */}
        <div className="p-4 rounded-xl bg-dark-900 border border-dark-700 space-y-2">
          <div className="flex items-center gap-2 text-xs font-mono font-semibold text-emerald-400">
            <BookOpen className="w-3.5 h-3.5" />
            <span>Learning Objectives</span>
          </div>
          <ul className="space-y-1.5">
            {lesson.objectives.map((obj, i) => (
              <li key={i} className="text-xs text-dark-300 flex items-start gap-2">
                <span className="text-emerald-500 mt-0.5">•</span>
                <span>{obj}</span>
              </li>
            ))}
          </ul>
        </div>

        {/* Prerequisites & Revision */}
        <div className="p-4 rounded-xl bg-dark-900 border border-dark-700 space-y-2">
          <div className="flex items-center gap-2 text-xs font-mono font-semibold text-cyan-400">
            <Clock className="w-3.5 h-3.5" />
            <span>Prerequisites & Revision Questions</span>
          </div>
          <div className="space-y-1.5">
            <div className="text-[11px] font-mono text-dark-400">Prerequisites:</div>
            <div className="flex flex-wrap gap-1.5">
              {lesson.prerequisites.map((p, i) => (
                <span
                  key={i}
                  className="px-2 py-0.5 rounded text-[10px] font-mono bg-dark-800 text-dark-300 border border-dark-700"
                >
                  {p}
                </span>
              ))}
            </div>

            {lesson.revision_questions.length > 0 && (
              <>
                <div className="text-[11px] font-mono text-dark-400 pt-1">Revision Check:</div>
                <ul className="space-y-1">
                  {lesson.revision_questions.map((rq, i) => (
                    <li key={i} className="text-xs text-dark-300 italic">
                      "{rq}"
                    </li>
                  ))}
                </ul>
              </>
            )}
          </div>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="flex items-center gap-1 border-b border-dark-700 overflow-x-auto pb-px">
        {[
          { id: 'concepts', label: 'Concept Deep-Dive', icon: BookOpen },
          { id: 'code', label: 'Runnable Code', icon: Code },
          { id: 'exercises', label: 'Exercises & Acceptance', icon: CheckCircle2 },
          { id: 'debugging', label: 'Common Errors & Edges', icon: AlertTriangle },
          { id: 'quiz', label: `Quiz (${lesson.quizzes.length})`, icon: HelpCircle },
          { id: 'neuromatrix', label: 'NeuroMatrix Project', icon: Shield },
          { id: 'notes', label: 'Study Notes', icon: FileText },
        ].map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              className={`flex items-center gap-2 px-3.5 py-2.5 text-xs font-mono border-b-2 transition-all whitespace-nowrap ${
                isActive
                  ? 'border-emerald-500 text-emerald-400 bg-emerald-500/5'
                  : 'border-transparent text-dark-400 hover:text-dark-200 hover:border-dark-600'
              }`}
            >
              <Icon className="w-3.5 h-3.5" />
              <span>{tab.label}</span>
            </button>
          );
        })}
      </div>

      {/* Tab Panels */}
      <div className="space-y-6 min-h-[400px]">
        {/* 1. Concepts Tab */}
        {activeTab === 'concepts' && (
          <div className="space-y-6">
            {lesson.concept_sections.map((sec, idx) => (
              <div key={idx} className="p-6 rounded-xl bg-dark-900 border border-dark-700 space-y-4">
                <h3 className="text-base font-bold text-dark-100 flex items-center gap-2">
                  <span className="w-2 h-2 rounded-full bg-emerald-400" />
                  {sec.title}
                </h3>
                <p className="text-sm text-dark-300 leading-relaxed whitespace-pre-line">
                  {sec.content}
                </p>

                {sec.key_points && sec.key_points.length > 0 && (
                  <div className="mt-4 pt-4 border-t border-dark-800 space-y-2">
                    <span className="text-xs font-mono text-dark-400 uppercase tracking-wider">
                      Key Takeaways:
                    </span>
                    <ul className="grid grid-cols-1 md:grid-cols-2 gap-2">
                      {sec.key_points.map((pt, pIdx) => (
                        <li
                          key={pIdx}
                          className="p-2.5 rounded bg-dark-950 border border-dark-800 text-xs text-dark-200 flex items-start gap-2"
                        >
                          <Check className="w-3.5 h-3.5 text-emerald-400 mt-0.5 shrink-0" />
                          <span>{pt}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}

        {/* 2. Runnable Code Tab */}
        {activeTab === 'code' && (
          <div className="space-y-6">
            {lesson.code_examples.map((ex, idx) => (
              <div key={idx} className="rounded-xl bg-dark-900 border border-dark-700 overflow-hidden">
                <div className="p-4 border-b border-dark-800 flex items-center justify-between">
                  <div>
                    <h4 className="text-sm font-bold text-dark-100">{ex.title}</h4>
                    <p className="text-xs text-dark-400 mt-0.5">{ex.description}</p>
                  </div>
                  <button
                    onClick={() => handleCopy(ex.code, `code-${idx}`)}
                    className="flex items-center gap-1.5 px-2.5 py-1 rounded bg-dark-800 hover:bg-dark-700 text-dark-300 text-xs font-mono transition-colors"
                  >
                    {copiedCodeId === `code-${idx}` ? (
                      <>
                        <Check className="w-3.5 h-3.5 text-emerald-400" />
                        <span className="text-emerald-400">Copied</span>
                      </>
                    ) : (
                      <>
                        <Copy className="w-3.5 h-3.5" />
                        <span>Copy</span>
                      </>
                    )}
                  </button>
                </div>

                {/* Code Block */}
                <div className="p-4 bg-dark-950 overflow-x-auto">
                  <pre className="font-mono text-xs text-emerald-300 leading-relaxed">
                    <code>{ex.code}</code>
                  </pre>
                </div>

                {/* Expected Output */}
                <div className="p-4 bg-dark-900 border-t border-dark-800 space-y-1">
                  <span className="text-[11px] font-mono text-dark-400 uppercase tracking-wider">
                    Expected Terminal Output:
                  </span>
                  <pre className="p-3 rounded bg-dark-950 border border-dark-800 font-mono text-xs text-dark-200">
                    {ex.expected_output}
                  </pre>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* 3. Exercises Tab */}
        {activeTab === 'exercises' && (
          <div className="space-y-6">
            {lesson.exercises.map((ex) => {
              const isSolutionVisible = showSolutions[ex.id] ?? false;
              const isPassed = exerciseStatus[ex.id] === 'passed';

              return (
                <div key={ex.id} className="p-6 rounded-xl bg-dark-900 border border-dark-700 space-y-4">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <span className="px-2 py-0.5 text-[10px] font-mono uppercase bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded">
                        {ex.difficulty}
                      </span>
                      <h3 className="text-base font-bold text-dark-100">{ex.title}</h3>
                    </div>

                    {isPassed && (
                      <span className="flex items-center gap-1 text-xs font-mono text-emerald-400">
                        <CheckCircle2 className="w-4 h-4" /> Passed
                      </span>
                    )}
                  </div>

                  <p className="text-sm text-dark-300 leading-relaxed">{ex.instructions}</p>

                  {/* Acceptance Criteria */}
                  {ex.acceptance_criteria && ex.acceptance_criteria.length > 0 && (
                    <div className="space-y-1.5 p-3 rounded-lg bg-dark-950 border border-dark-800">
                      <span className="text-xs font-mono text-dark-400">Acceptance Criteria:</span>
                      <ul className="space-y-1">
                        {ex.acceptance_criteria.map((crit, cIdx) => (
                          <li key={cIdx} className="text-xs text-dark-300 flex items-start gap-2">
                            <span className="text-emerald-400">✓</span>
                            <span>{crit}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {/* Starter Code */}
                  <div className="space-y-1.5">
                    <div className="flex items-center justify-between text-xs font-mono text-dark-400">
                      <span>Starter Template:</span>
                      <button
                        onClick={() => handleCopy(ex.starter_code, `starter-${ex.id}`)}
                        className="text-emerald-400 hover:underline flex items-center gap-1"
                      >
                        <Copy className="w-3 h-3" /> Copy Template
                      </button>
                    </div>
                    <pre className="p-3 rounded-lg bg-dark-950 border border-dark-800 font-mono text-xs text-dark-200 overflow-x-auto">
                      <code>{ex.starter_code}</code>
                    </pre>
                  </div>

                  {/* Local Execution Output Recorder */}
                  <div className="space-y-2 pt-2 border-t border-dark-800">
                    <label className="block text-xs font-mono text-dark-300">
                      Run locally in your terminal and record your verified output:
                    </label>
                    <textarea
                      rows={3}
                      value={submittedOutputs[ex.id] || ''}
                      onChange={(e) =>
                        setSubmittedOutputs({ ...submittedOutputs, [ex.id]: e.target.value })
                      }
                      placeholder="Paste your script's terminal output here..."
                      className="w-full p-3 rounded-lg bg-dark-950 border border-dark-700 font-mono text-xs text-dark-200 placeholder-dark-600 focus:outline-none focus:border-emerald-500"
                    />
                    <input
                      type="text"
                      value={exerciseNotes[ex.id] || ''}
                      onChange={(e) =>
                        setExerciseNotes({ ...exerciseNotes, [ex.id]: e.target.value })
                      }
                      placeholder="Optional notes or execution flags used..."
                      className="w-full p-2 rounded-lg bg-dark-950 border border-dark-700 font-mono text-xs text-dark-200 placeholder-dark-600 focus:outline-none focus:border-emerald-500"
                    />

                    <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
                      <button
                        onClick={() =>
                          setShowSolutions((prev) => ({ ...prev, [ex.id]: !isSolutionVisible }))
                        }
                        className="flex items-center gap-1.5 text-xs font-mono text-dark-400 hover:text-dark-200"
                      >
                        {isSolutionVisible ? <EyeOff className="w-3.5 h-3.5" /> : <Eye className="w-3.5 h-3.5" />}
                        <span>{isSolutionVisible ? 'Hide Reference Solution' : 'Reveal Reference Solution'}</span>
                      </button>

                      <button
                        onClick={() => handleExerciseSubmit(ex.id)}
                        className="px-4 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-600 text-black font-semibold text-xs font-mono transition-all flex items-center gap-2"
                      >
                        <Check className="w-3.5 h-3.5" />
                        <span>Record Verified Exercise</span>
                      </button>
                    </div>

                    {isSolutionVisible && (
                      <div className="mt-3 p-4 rounded-lg bg-emerald-950/20 border border-emerald-500/30 space-y-2">
                        <span className="text-xs font-mono font-semibold text-emerald-400">
                          Reference Solution:
                        </span>
                        <pre className="p-3 rounded bg-dark-950 font-mono text-xs text-emerald-300 overflow-x-auto">
                          <code>{ex.solution_code}</code>
                        </pre>
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        )}

        {/* 4. Common Errors & Debugging Tab */}
        {activeTab === 'debugging' && (
          <div className="space-y-6">
            <div className="p-6 rounded-xl bg-dark-900 border border-dark-700 space-y-4">
              <h3 className="text-base font-bold text-dark-100 flex items-center gap-2">
                <AlertTriangle className="w-4 h-4 text-amber-400" />
                <span>Common Errors & Root Cause Analysis</span>
              </h3>

              <div className="space-y-4">
                {lesson.common_errors.map((err, idx) => (
                  <div key={idx} className="p-4 rounded-lg bg-dark-950 border border-dark-800 space-y-2">
                    <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-red-500/10 text-red-400 border border-red-500/30">
                      {err.error_type}
                    </span>
                    <div className="text-xs text-dark-300">
                      <strong className="text-dark-200">Root Cause:</strong> {err.cause}
                    </div>
                    <div className="text-xs text-dark-300">
                      <strong className="text-emerald-400">The Fix:</strong> {err.fix}
                    </div>
                    {err.example && (
                      <pre className="p-2.5 rounded bg-dark-900 font-mono text-[11px] text-dark-400 mt-1">
                        {err.example}
                      </pre>
                    )}
                  </div>
                ))}
              </div>

              {lesson.edge_cases && lesson.edge_cases.length > 0 && (
                <div className="pt-4 border-t border-dark-800 space-y-2">
                  <h4 className="text-xs font-mono uppercase text-dark-400">Edge Cases to Consider:</h4>
                  <ul className="space-y-1">
                    {lesson.edge_cases.map((ec, idx) => (
                      <li key={idx} className="text-xs text-dark-300 flex items-start gap-2">
                        <span className="text-amber-400">!</span>
                        <span>{ec}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </div>
        )}

        {/* 5. Knowledge Quiz Tab */}
        {activeTab === 'quiz' && (
          <div className="p-6 rounded-xl bg-dark-900 border border-dark-700 space-y-6">
            <div className="flex items-center justify-between border-b border-dark-800 pb-4">
              <div>
                <h3 className="text-base font-bold text-dark-100 flex items-center gap-2">
                  <HelpCircle className="w-4 h-4 text-emerald-400" />
                  <span>Day {lesson.day_number} Knowledge Check</span>
                </h3>
                <p className="text-xs text-dark-400 mt-0.5">
                  Answer the questions to verify your conceptual comprehension.
                </p>
              </div>

              {quizResult && (
                <div className="text-right">
                  <div className="text-lg font-bold font-mono text-emerald-400">
                    {quizResult.correct_count} / {quizResult.total_questions} ({quizResult.score_percentage}%)
                  </div>
                  <div className="text-[11px] font-mono text-dark-400">Score Recorded</div>
                </div>
              )}
            </div>

            <div className="space-y-6">
              {lesson.quizzes.map((q, idx) => {
                const selected = quizSelections[q.id];
                const evaluated = quizResult?.results.find((r) => r.question_id === q.id);

                return (
                  <div key={q.id} className="p-4 rounded-lg bg-dark-950 border border-dark-800 space-y-3">
                    <div className="flex items-start justify-between gap-4">
                      <h4 className="text-sm font-semibold text-dark-100">
                        {idx + 1}. {q.question_text}
                      </h4>
                      <span className="px-2 py-0.5 text-[10px] font-mono uppercase bg-dark-800 text-dark-400 rounded shrink-0">
                        {q.question_type}
                      </span>
                    </div>

                    {q.code_snippet && (
                      <pre className="p-3 rounded bg-dark-900 font-mono text-xs text-emerald-300 overflow-x-auto">
                        <code>{q.code_snippet}</code>
                      </pre>
                    )}

                    {/* Radio Options */}
                    <div className="space-y-2 pt-1">
                      {q.options.map((opt, oIdx) => {
                        const isChecked = selected === opt;
                        let optionStyle = 'border-dark-800 hover:border-dark-700 bg-dark-900 text-dark-300';

                        if (evaluated) {
                          if (opt === evaluated.correct_answer) {
                            optionStyle = 'border-emerald-500/60 bg-emerald-950/20 text-emerald-300';
                          } else if (isChecked && !evaluated.is_correct) {
                            optionStyle = 'border-red-500/60 bg-red-950/20 text-red-300';
                          }
                        } else if (isChecked) {
                          optionStyle = 'border-emerald-500 bg-emerald-500/10 text-emerald-300';
                        }

                        return (
                          <label
                            key={oIdx}
                            className={`flex items-center gap-3 p-3 rounded-lg border cursor-pointer text-xs transition-all ${optionStyle}`}
                          >
                            <input
                              type="radio"
                              name={q.id}
                              value={opt}
                              checked={isChecked}
                              disabled={quizSubmitting || quizResult !== null}
                              onChange={() =>
                                setQuizSelections((prev) => ({ ...prev, [q.id]: opt }))
                              }
                              className="accent-emerald-500"
                            />
                            <span>{opt}</span>
                          </label>
                        );
                      })}
                    </div>

                    {/* Answer Explanation */}
                    {evaluated && (
                      <div className="mt-3 p-3 rounded bg-dark-900 border border-dark-800 text-xs text-dark-300 space-y-1">
                        <span className="font-mono font-semibold text-emerald-400">
                          {evaluated.is_correct ? '✓ Correct!' : '✗ Explanation:'}
                        </span>
                        <p>{evaluated.explanation}</p>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            <div className="flex items-center justify-between pt-4 border-t border-dark-800">
              {quizResult ? (
                <button
                  onClick={() => {
                    setQuizResult(null);
                    setQuizSelections({});
                  }}
                  className="px-4 py-2 rounded-lg bg-dark-800 hover:bg-dark-700 text-xs font-mono text-dark-300 flex items-center gap-2"
                >
                  <RotateCcw className="w-3.5 h-3.5" /> Retake Quiz
                </button>
              ) : (
                <button
                  onClick={handleQuizSubmit}
                  disabled={quizSubmitting}
                  className="px-6 py-2.5 rounded-lg bg-emerald-500 hover:bg-emerald-600 text-black font-semibold text-xs font-mono transition-all flex items-center gap-2 ml-auto"
                >
                  <Send className="w-3.5 h-3.5" />
                  <span>{quizSubmitting ? 'Evaluating...' : 'Submit Answers'}</span>
                </button>
              )}
            </div>
          </div>
        )}

        {/* 6. NeuroMatrix Project Connection Tab */}
        {activeTab === 'neuromatrix' && (
          <div className="p-6 rounded-xl bg-dark-900 border border-dark-700 space-y-5">
            <div className="flex items-center gap-3">
              <div className="w-9 h-9 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                <Shield className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-base font-bold text-dark-100">
                  {lesson.neuromatrix_integration.topic}
                </h3>
                <span className="text-xs font-mono text-emerald-400">
                  Target Component: {lesson.neuromatrix_integration.target_component}
                </span>
              </div>
            </div>

            <div className="p-4 rounded-lg bg-dark-950 border border-dark-800 space-y-2">
              <span className="text-xs font-mono text-dark-400 uppercase tracking-wider">
                Engineering Context:
              </span>
              <p className="text-xs text-dark-300 leading-relaxed">
                {lesson.neuromatrix_integration.context}
              </p>
            </div>

            <div className="p-4 rounded-lg bg-dark-950 border border-dark-800 space-y-2">
              <span className="text-xs font-mono text-dark-400 uppercase tracking-wider">
                Project Integration Task:
              </span>
              <p className="text-xs text-dark-200 leading-relaxed">
                {lesson.neuromatrix_integration.task_description}
              </p>
            </div>

            <div className="p-4 rounded-lg bg-dark-950 border border-dark-800 space-y-2">
              <span className="text-xs font-mono text-dark-400 uppercase tracking-wider">
                Verification Step:
              </span>
              <p className="text-xs text-emerald-400 font-mono">
                {lesson.neuromatrix_integration.verification_step}
              </p>
            </div>

            <div className="pt-2">
              <Link
                to="/projects"
                className="inline-flex items-center gap-2 text-xs font-mono text-emerald-400 hover:underline"
              >
                <span>Open NeuroMatrix Project Lab to track commits and milestone status</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>
          </div>
        )}

        {/* 7. Study Notes Tab */}
        {activeTab === 'notes' && (
          <div className="p-6 rounded-xl bg-dark-900 border border-dark-700 space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-base font-bold text-dark-100 flex items-center gap-2">
                  <FileText className="w-4 h-4 text-emerald-400" />
                  <span>Personal Study Notes for Day {lesson.day_number}</span>
                </h3>
                <p className="text-xs text-dark-400 mt-0.5">
                  Record your key insights, commands, and reminders. Persisted safely across browser refreshes.
                </p>
              </div>

              {noteSaved && (
                <span className="flex items-center gap-1 text-xs font-mono text-emerald-400 animate-fade-in">
                  <Check className="w-3.5 h-3.5" /> Saved!
                </span>
              )}
            </div>

            <textarea
              rows={12}
              value={noteContent}
              onChange={(e) => setNoteContent(e.target.value)}
              placeholder="Write your notes here in markdown or plain text..."
              className="w-full p-4 rounded-xl bg-dark-950 border border-dark-700 font-mono text-xs text-dark-200 placeholder-dark-600 focus:outline-none focus:border-emerald-500 leading-relaxed"
            />

            <div className="flex items-center justify-between pt-2">
              <span className="text-[11px] font-mono text-dark-500">
                {noteContent.length} characters
              </span>
              <button
                onClick={handleSaveNote}
                disabled={noteSaving}
                className="px-5 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-600 text-black font-semibold text-xs font-mono transition-all flex items-center gap-2"
              >
                <Check className="w-3.5 h-3.5" />
                <span>{noteSaving ? 'Saving...' : 'Save Notes'}</span>
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Bottom Navigation: Previous Day & Next Day */}
      <div className="flex items-center justify-between pt-6 border-t border-dark-700">
        {lesson.prev_day ? (
          <Link
            to={`/curriculum/${lesson.prev_day}`}
            className="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-dark-900 border border-dark-700 hover:border-dark-600 text-dark-300 hover:text-dark-100 text-xs font-mono transition-all"
          >
            <ChevronLeft className="w-4 h-4 text-emerald-400" />
            <span>Previous: Day {lesson.prev_day}</span>
          </Link>
        ) : (
          <div />
        )}

        {lesson.next_day && (
          <Link
            to={`/curriculum/${lesson.next_day}`}
            className="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-dark-900 border border-dark-700 hover:border-dark-600 text-dark-300 hover:text-dark-100 text-xs font-mono transition-all"
          >
            <span>Next: Day {lesson.next_day}</span>
            <ChevronRight className="w-4 h-4 text-emerald-400" />
          </Link>
        )}
      </div>
    </div>
  );
};
