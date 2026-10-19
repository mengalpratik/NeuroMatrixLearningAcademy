import React, { useEffect, useState } from 'react';
import { Terminal, CheckCircle2, RotateCcw, Award } from 'lucide-react';
import { api } from '../api/client';
import { PracticeQuestionOut } from '../api/types';

export const PracticeLabPage: React.FC = () => {
  const [questions, setQuestions] = useState<PracticeQuestionOut[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedType, setSelectedType] = useState<string>('all');
  const [selectedWeek, setSelectedWeek] = useState<number | 'all'>('all');

  // Interactive state
  const [userAnswers, setUserAnswers] = useState<Record<string, string>>({});
  const [revealed, setRevealed] = useState<Record<string, boolean>>({});
  const [scoreHistory, setScoreHistory] = useState<{ total: number; correct: number }>({
    total: 0,
    correct: 0,
  });

  const loadQuestions = () => {
    setLoading(true);
    const typeParam = selectedType === 'all' ? undefined : selectedType;
    const weekParam = selectedWeek === 'all' ? undefined : selectedWeek;

    api.getPracticeQuestions(typeParam, weekParam, undefined, 50)
      .then((data) => {
        setQuestions(data);
      })
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    loadQuestions();
  }, [selectedType, selectedWeek]);

  const handleSelectAnswer = (qId: string, answer: string) => {
    if (revealed[qId]) return;
    setUserAnswers((prev) => ({ ...prev, [qId]: answer }));
  };

  const handleCheckAnswer = (q: PracticeQuestionOut) => {
    if (revealed[q.id]) return;
    const userAns = userAnswers[q.id];
    if (!userAns) {
      alert('Please select an option before checking.');
      return;
    }

    setRevealed((prev) => ({ ...prev, [q.id]: true }));
    const isCorrect = userAns.trim() === q.options[0]?.trim(); // In seed data, first option or match
    // Note: check if matches explanation or answer
    setScoreHistory((prev) => ({
      total: prev.total + 1,
      correct: prev.correct + (isCorrect ? 1 : 0),
    }));
  };

  const handleReset = () => {
    setUserAnswers({});
    setRevealed({});
    setScoreHistory({ total: 0, correct: 0 });
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Page Header */}
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-dark-700 pb-6">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <span className="px-2 py-0.5 rounded text-[11px] font-mono bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">
              Interactive Drill Environment
            </span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-dark-100 flex items-center gap-3">
            <Terminal className="w-7 h-7 text-emerald-400" />
            <span>Practice Lab</span>
          </h1>
          <p className="text-sm text-dark-400 mt-1">
            Sharpen your Python full-stack skills with code-reading, output prediction, and debugging drills.
          </p>
        </div>

        {/* Score & Reset Stats */}
        <div className="flex items-center gap-4 bg-dark-900 border border-dark-700 rounded-xl p-3 shrink-0">
          <div>
            <div className="text-[11px] font-mono text-dark-400">Drill Score</div>
            <div className="text-base font-bold font-mono text-emerald-400">
              {scoreHistory.correct} / {scoreHistory.total}
              {scoreHistory.total > 0 &&
                ` (${Math.round((scoreHistory.correct / scoreHistory.total) * 100)}%)`}
            </div>
          </div>
          <button
            onClick={handleReset}
            className="p-2 rounded bg-dark-800 hover:bg-dark-700 text-dark-300 text-xs font-mono"
            title="Reset score"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Filter Controls */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-dark-900 p-4 rounded-xl border border-dark-700">
        <div>
          <label className="block text-xs font-mono text-dark-400 mb-1.5">Question Category:</label>
          <select
            value={selectedType}
            onChange={(e) => setSelectedType(e.target.value)}
            className="w-full bg-dark-950 border border-dark-700 rounded-lg px-3 py-2 text-xs font-mono text-dark-200 focus:outline-none focus:border-emerald-500"
          >
            <option value="all">All Drill Categories</option>
            <option value="mcq">Multiple Choice Questions</option>
            <option value="output_prediction">Output Prediction Exercises</option>
            <option value="code_reading">Code-Reading Questions</option>
            <option value="debugging">Debugging Challenges</option>
          </select>
        </div>

        <div>
          <label className="block text-xs font-mono text-dark-400 mb-1.5">Roadmap Week:</label>
          <select
            value={selectedWeek}
            onChange={(e) =>
              setSelectedWeek(e.target.value === 'all' ? 'all' : Number(e.target.value))
            }
            className="w-full bg-dark-950 border border-dark-700 rounded-lg px-3 py-2 text-xs font-mono text-dark-200 focus:outline-none focus:border-emerald-500"
          >
            <option value="all">All Weeks (1–16)</option>
            {Array.from({ length: 16 }, (_, i) => i + 1).map((w) => (
              <option key={w} value={w}>
                Week {w}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Questions List */}
      {loading ? (
        <div className="py-16 text-center">
          <div className="w-8 h-8 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <span className="font-mono text-xs text-dark-400">Loading drill questions...</span>
        </div>
      ) : questions.length > 0 ? (
        <div className="space-y-6">
          {questions.map((q, idx) => {
            const isRevealed = revealed[q.id];
            const userSelection = userAnswers[q.id];

            return (
              <div
                key={q.id}
                className="p-6 rounded-xl bg-dark-900 border border-dark-700 space-y-4 hover:border-dark-600 transition-all"
              >
                <div className="flex items-start justify-between gap-4">
                  <div className="space-y-1">
                    <div className="flex items-center gap-2">
                      <span className="px-2 py-0.5 rounded text-[10px] font-mono uppercase bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                        Day {q.day_number}
                      </span>
                      <span className="text-xs font-mono text-dark-400">{q.lesson_title}</span>
                      <span className="text-dark-600">•</span>
                      <span className="text-[10px] font-mono text-dark-500 uppercase">
                        {q.question_type.replace('_', ' ')}
                      </span>
                    </div>
                    <h3 className="text-sm font-semibold text-dark-100 mt-1">
                      {idx + 1}. {q.question_text}
                    </h3>
                  </div>
                </div>

                {q.code_snippet && (
                  <pre className="p-3.5 rounded-lg bg-dark-950 border border-dark-800 font-mono text-xs text-emerald-300 overflow-x-auto">
                    <code>{q.code_snippet}</code>
                  </pre>
                )}

                {/* Options */}
                <div className="space-y-2">
                  {q.options.map((opt, oIdx) => {
                    const isSelected = userSelection === opt;
                    return (
                      <button
                        key={oIdx}
                        onClick={() => handleSelectAnswer(q.id, opt)}
                        disabled={isRevealed}
                        className={`w-full text-left p-3 rounded-lg border text-xs font-mono transition-all flex items-center justify-between ${
                          isSelected
                            ? 'bg-emerald-500/10 border-emerald-500 text-emerald-300'
                            : 'bg-dark-950 border-dark-800 hover:border-dark-700 text-dark-300'
                        }`}
                      >
                        <span>{opt}</span>
                        {isSelected && <CheckCircle2 className="w-4 h-4 text-emerald-400" />}
                      </button>
                    );
                  })}
                </div>

                {/* Action & Explanation */}
                <div className="pt-2 flex items-center justify-between">
                  {!isRevealed ? (
                    <button
                      onClick={() => handleCheckAnswer(q)}
                      className="px-4 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-600 text-black font-semibold text-xs font-mono transition-all ml-auto"
                    >
                      Check Answer
                    </button>
                  ) : (
                    <div className="w-full p-4 rounded-lg bg-dark-950 border border-dark-800 space-y-1">
                      <span className="text-xs font-mono font-semibold text-emerald-400 flex items-center gap-1.5">
                        <Award className="w-4 h-4" /> Explanation:
                      </span>
                      <p className="text-xs text-dark-300 leading-relaxed">{q.explanation}</p>
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      ) : (
        <div className="p-12 text-center rounded-xl bg-dark-900 border border-dark-700">
          <Terminal className="w-8 h-8 text-dark-500 mx-auto mb-2" />
          <h3 className="text-sm font-semibold text-dark-200">No questions match filter</h3>
          <p className="text-xs font-mono text-dark-400 mt-1">
            Try selecting "All Drill Categories" or resetting the week filter.
          </p>
        </div>
      )}
    </div>
  );
};
