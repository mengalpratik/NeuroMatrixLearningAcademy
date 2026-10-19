import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import {
  Play,
  CheckCircle2,
  Clock,
  BookOpen,
  Award,
  Terminal,
  Shield,
  Bookmark,
  ArrowRight,
  TrendingUp,
  Activity,
} from 'lucide-react';
import { api } from '../api/client';
import { DashboardSummaryOut } from '../api/types';

export const DashboardPage: React.FC = () => {
  const [summary, setSummary] = useState<DashboardSummaryOut | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let mounted = true;
    api.getDashboardSummary()
      .then((data) => {
        if (mounted) setSummary(data);
      })
      .catch((err) => {
        if (mounted) setError(err.message);
      })
      .finally(() => {
        if (mounted) setLoading(false);
      });
    return () => {
      mounted = false;
    };
  }, []);

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-12 flex flex-col items-center justify-center min-h-[50vh]">
        <div className="w-8 h-8 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mb-4" />
        <span className="font-mono text-sm text-dark-400">Loading NeuroMatrix telemetry...</span>
      </div>
    );
  }

  if (error || !summary) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-12">
        <div className="p-6 rounded-xl bg-red-950/20 border border-red-500/30 text-center">
          <h3 className="text-red-400 font-semibold mb-2">Failed to load dashboard metrics</h3>
          <p className="text-xs text-dark-300 font-mono mb-4">{error}</p>
          <button
            onClick={() => window.location.reload()}
            className="px-4 py-2 bg-dark-800 hover:bg-dark-700 text-xs font-mono rounded text-dark-200"
          >
            Retry Connection
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Hero Overview Card */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-dark-900 to-dark-850 border border-dark-700 p-6 sm:p-8">
        <div className="absolute top-0 right-0 w-96 h-96 bg-emerald-500/5 rounded-full blur-3xl pointer-events-none" />

        <div className="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="space-y-3 max-w-2xl">
            <div className="flex flex-wrap items-center gap-2">
              <span className="px-2 py-0.5 rounded text-[11px] font-mono uppercase bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                Phase {summary.current_phase} • Week {summary.current_week}
              </span>
              <span className="px-2 py-0.5 rounded text-[11px] font-mono bg-dark-800 text-dark-300 border border-dark-700">
                Day {summary.current_day} of {summary.total_days}
              </span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-dark-100">
              NeuroMatrix Learning Academy
            </h1>
            <p className="text-sm text-dark-400 leading-relaxed">
              Master full-stack Python engineering from low-level systems and async protocols to modern React interfaces and production DevOps across 112 dedicated days.
            </p>
          </div>

          {/* Continue Learning CTA */}
          <div className="flex flex-col sm:flex-row lg:flex-col gap-3 shrink-0">
            <Link
              to={`/curriculum/${summary.current_day}`}
              className="inline-flex items-center justify-center gap-2.5 px-6 py-3 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-black font-semibold text-sm transition-all shadow-cyber-sm hover:shadow-cyber-md"
            >
              <Play className="w-4 h-4 fill-black" />
              <span>Continue Day {summary.current_day}</span>
              <ArrowRight className="w-4 h-4" />
            </Link>

            <Link
              to="/curriculum"
              className="inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-dark-800 hover:bg-dark-700 text-dark-200 text-xs font-mono border border-dark-700 transition-colors"
            >
              <BookOpen className="w-3.5 h-3.5 text-emerald-400" />
              <span>Curriculum Explorer</span>
            </Link>
          </div>
        </div>

        {/* Global Progress Bar */}
        <div className="mt-8 pt-6 border-t border-dark-800/80">
          <div className="flex items-center justify-between text-xs font-mono mb-2">
            <span className="text-dark-400 flex items-center gap-1.5">
              <TrendingUp className="w-3.5 h-3.5 text-emerald-400" />
              Roadmap Progress: {summary.completed_days} / {summary.total_days} Days Completed
            </span>
            <span className="font-bold text-emerald-400">{summary.completion_percentage}%</span>
          </div>
          <div className="w-full h-2.5 bg-dark-800 rounded-full overflow-hidden p-0.5 border border-dark-700">
            <div
              className="h-full bg-gradient-to-r from-emerald-600 to-emerald-400 rounded-full transition-all duration-500"
              style={{ width: `${Math.max(summary.completion_percentage, 0.5)}%` }}
            />
          </div>
        </div>
      </div>

      {/* Metrics Row */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div className="p-4 rounded-xl bg-dark-900 border border-dark-700">
          <div className="text-xs text-dark-400 font-mono">Current Focus</div>
          <div className="text-xl font-bold font-mono text-dark-100 mt-1">
            Day {summary.current_day}
          </div>
          <div className="text-[11px] text-dark-500 font-mono mt-0.5">
            Week {summary.current_week} • Phase {summary.current_phase}
          </div>
        </div>

        <div className="p-4 rounded-xl bg-dark-900 border border-dark-700">
          <div className="text-xs text-dark-400 font-mono">Lessons Completed</div>
          <div className="text-xl font-bold font-mono text-emerald-400 mt-1">
            {summary.completed_days}
          </div>
          <div className="text-[11px] text-dark-500 font-mono mt-0.5">
            {summary.remaining_days} remaining
          </div>
        </div>

        <div className="p-4 rounded-xl bg-dark-900 border border-dark-700">
          <div className="text-xs text-dark-400 font-mono">In Progress</div>
          <div className="text-xl font-bold font-mono text-amber-400 mt-1">
            {summary.in_progress_days}
          </div>
          <div className="text-[11px] text-dark-500 font-mono mt-0.5">Active studies</div>
        </div>

        <div className="p-4 rounded-xl bg-dark-900 border border-dark-700">
          <div className="text-xs text-dark-400 font-mono">Bookmarks & Notes</div>
          <div className="text-xl font-bold font-mono text-cyan-400 mt-1">
            {summary.bookmarked_count + summary.notes_count}
          </div>
          <div className="text-[11px] text-dark-500 font-mono mt-0.5">
            {summary.bookmarked_count} saved, {summary.notes_count} notes
          </div>
        </div>
      </div>

      {/* Main Content Grid: Today's Lesson & Milestones */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Today's Target Lesson */}
        <div className="lg:col-span-2 space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-base font-semibold text-dark-100 flex items-center gap-2">
              <Clock className="w-4 h-4 text-emerald-400" />
              <span>Today's Target Lesson</span>
            </h2>
            <span className="text-xs font-mono text-dark-400">
              Est. {summary.today_lesson?.duration_minutes || 60} mins
            </span>
          </div>

          {summary.today_lesson ? (
            <div className="p-6 rounded-xl bg-dark-900 border border-dark-700 hover:border-dark-600 transition-all space-y-4">
              <div className="flex items-start justify-between gap-4">
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <span className="px-2 py-0.5 text-[10px] font-mono uppercase bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded">
                      Day {summary.today_lesson.day_number}
                    </span>
                    <span className="text-xs text-dark-400 font-mono">
                      Week {summary.today_lesson.week_number}
                    </span>
                  </div>
                  <h3 className="text-lg font-bold text-dark-100 hover:text-emerald-400 transition-colors">
                    <Link to={`/curriculum/${summary.today_lesson.day_number}`}>
                      {summary.today_lesson.title}
                    </Link>
                  </h3>
                </div>

                <div className="shrink-0">
                  {summary.today_lesson.status === 'completed' ? (
                    <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded text-xs font-mono bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                      <CheckCircle2 className="w-3.5 h-3.5" /> Completed
                    </span>
                  ) : summary.today_lesson.status === 'in_progress' ? (
                    <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded text-xs font-mono bg-amber-500/10 text-amber-400 border border-amber-500/30">
                      <Clock className="w-3.5 h-3.5" /> In Progress
                    </span>
                  ) : (
                    <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded text-xs font-mono bg-dark-800 text-dark-400 border border-dark-700">
                      Not Started
                    </span>
                  )}
                </div>
              </div>

              <p className="text-sm text-dark-300 leading-relaxed">
                {summary.today_lesson.summary}
              </p>

              <div className="pt-2 flex items-center justify-between border-t border-dark-800">
                <Link
                  to={`/curriculum/${summary.today_lesson.day_number}`}
                  className="inline-flex items-center gap-1.5 text-xs font-medium text-emerald-400 hover:text-emerald-300 transition-colors"
                >
                  <span>Open Lesson Workspace</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </Link>
              </div>
            </div>
          ) : (
            <div className="p-8 rounded-xl bg-dark-900 border border-dark-700 text-center font-mono text-xs text-dark-400">
              All 112 days completed! Outstanding engineering achievement.
            </div>
          )}

          {/* Quick Action Navigation Grid */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2">
            <Link
              to="/curriculum"
              className="p-3.5 rounded-xl bg-dark-900 border border-dark-700 hover:border-emerald-500/40 hover:bg-dark-850 transition-all text-left group"
            >
              <BookOpen className="w-4 h-4 text-emerald-400 mb-2 group-hover:scale-110 transition-transform" />
              <div className="text-xs font-medium text-dark-200 group-hover:text-emerald-300">
                Curriculum
              </div>
              <div className="text-[10px] text-dark-500 font-mono mt-0.5">16 Weeks, 112 Days</div>
            </Link>

            <Link
              to="/practice"
              className="p-3.5 rounded-xl bg-dark-900 border border-dark-700 hover:border-emerald-500/40 hover:bg-dark-850 transition-all text-left group"
            >
              <Terminal className="w-4 h-4 text-cyan-400 mb-2 group-hover:scale-110 transition-transform" />
              <div className="text-xs font-medium text-dark-200 group-hover:text-cyan-300">
                Practice Lab
              </div>
              <div className="text-[10px] text-dark-500 font-mono mt-0.5">Drills & Quizzes</div>
            </Link>

            <Link
              to="/projects"
              className="p-3.5 rounded-xl bg-dark-900 border border-dark-700 hover:border-emerald-500/40 hover:bg-dark-850 transition-all text-left group"
            >
              <Shield className="w-4 h-4 text-emerald-400 mb-2 group-hover:scale-110 transition-transform" />
              <div className="text-xs font-medium text-dark-200 group-hover:text-emerald-300">
                Project Lab
              </div>
              <div className="text-[10px] text-dark-500 font-mono mt-0.5">16 Milestones</div>
            </Link>

            <Link
              to="/notes"
              className="p-3.5 rounded-xl bg-dark-900 border border-dark-700 hover:border-emerald-500/40 hover:bg-dark-850 transition-all text-left group"
            >
              <Bookmark className="w-4 h-4 text-amber-400 mb-2 group-hover:scale-110 transition-transform" />
              <div className="text-xs font-medium text-dark-200 group-hover:text-amber-300">
                Study Notes
              </div>
              <div className="text-[10px] text-dark-500 font-mono mt-0.5">Saved Reference</div>
            </Link>
          </div>
        </div>

        {/* Sidebar: Weekly Milestones & Recent Activity */}
        <div className="space-y-6">
          {/* Milestone Statuses */}
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <h2 className="text-base font-semibold text-dark-100 flex items-center gap-2">
                <Award className="w-4 h-4 text-emerald-400" />
                <span>Weekly Milestones</span>
              </h2>
              <Link to="/projects" className="text-xs font-mono text-emerald-400 hover:underline">
                View All
              </Link>
            </div>

            <div className="space-y-2">
              {summary.weekly_milestones.slice(0, 4).map((m) => (
                <div
                  key={m.week_number}
                  className="p-3 rounded-lg bg-dark-900 border border-dark-700 flex items-center justify-between"
                >
                  <div className="flex items-center gap-2.5">
                    <span className="font-mono text-xs text-dark-400">Week {m.week_number}</span>
                    <span className="text-xs text-dark-200">
                      {m.week_number === 1
                        ? 'Device Status CLI'
                        : m.week_number === 2
                        ? 'Task Registry'
                        : m.week_number === 3
                        ? 'Node Agent Core'
                        : 'Static Dashboard'}
                    </span>
                  </div>

                  <span
                    className={`px-2 py-0.5 text-[10px] font-mono rounded ${
                      m.status === 'verified'
                        ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30'
                        : m.status === 'ready_for_review'
                        ? 'bg-cyan-500/10 text-cyan-400 border border-cyan-500/30'
                        : m.status === 'in_progress'
                        ? 'bg-amber-500/10 text-amber-400 border border-amber-500/30'
                        : 'bg-dark-800 text-dark-500'
                    }`}
                  >
                    {m.status.replace('_', ' ')}
                  </span>
                </div>
              ))}
            </div>
          </div>

          {/* Recent Activity Feed */}
          <div className="space-y-3">
            <h2 className="text-base font-semibold text-dark-100 flex items-center gap-2">
              <Activity className="w-4 h-4 text-emerald-400" />
              <span>Recent Activity</span>
            </h2>

            <div className="p-4 rounded-xl bg-dark-900 border border-dark-700 divide-y divide-dark-800">
              {summary.recent_activities.length > 0 ? (
                summary.recent_activities.slice(0, 5).map((act) => (
                  <div key={act.id} className="py-2.5 first:pt-0 last:pb-0">
                    <div className="text-xs text-dark-200">{act.summary}</div>
                    <div className="text-[10px] text-dark-500 font-mono mt-0.5">
                      {new Date(act.created_at).toLocaleTimeString([], {
                        hour: '2-digit',
                        minute: '2-digit',
                      })}
                    </div>
                  </div>
                ))
              ) : (
                <div className="text-center py-4 text-xs font-mono text-dark-500">
                  No learning activity recorded yet. Start Day 1 to initialize your log!
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
