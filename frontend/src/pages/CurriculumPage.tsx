import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import {
  BookOpen,
  Search,
  CheckCircle2,
  Clock,
  ChevronDown,
  ChevronUp,
  Bookmark,
  Award,
  ArrowRight,
} from 'lucide-react';
import { api } from '../api/client';
import { CurriculumOverviewOut } from '../api/types';

export const CurriculumPage: React.FC = () => {
  const [overview, setOverview] = useState<CurriculumOverviewOut | null>(null);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedPhase, setSelectedPhase] = useState<number | 'all'>('all');
  const [selectedStatus, setSelectedStatus] = useState<string>('all');
  const [expandedWeeks, setExpandedWeeks] = useState<Record<number, boolean>>({
    1: true,
    2: true,
  });

  const loadData = () => {
    api.getCurriculumOverview()
      .then((data) => {
        setOverview(data);
      })
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    loadData();
  }, []);

  const toggleWeek = (weekNumber: number) => {
    setExpandedWeeks((prev) => ({
      ...prev,
      [weekNumber]: !prev[weekNumber],
    }));
  };

  const handleToggleBookmark = async (dayNumber: number, e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    try {
      await api.toggleBookmark(dayNumber);
      loadData();
    } catch (err) {
      console.error(err);
    }
  };

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-16 flex flex-col items-center justify-center min-h-[50vh]">
        <div className="w-8 h-8 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mb-4" />
        <span className="font-mono text-sm text-dark-400">Loading full 112-day curriculum...</span>
      </div>
    );
  }

  // Filter weeks and lessons
  const filteredPhases = overview?.phases.map((phase) => {
    if (selectedPhase !== 'all' && phase.phase_number !== selectedPhase) {
      return null;
    }

    const filteredWeeks = phase.weeks.map((week) => {
      const filteredLessons = week.lessons.filter((lesson) => {
        // Status filter
        if (selectedStatus !== 'all' && lesson.status !== selectedStatus) {
          return false;
        }

        // Search query filter
        if (searchQuery.trim()) {
          const q = searchQuery.toLowerCase();
          const matchTitle = lesson.title.toLowerCase().includes(q);
          const matchSummary = lesson.summary.toLowerCase().includes(q);
          const matchDay = `day ${lesson.day_number}`.includes(q);
          return matchTitle || matchSummary || matchDay;
        }

        return true;
      });

      return {
        ...week,
        filteredLessons,
      };
    }).filter((w) => w.filteredLessons.length > 0 || !searchQuery);

    return {
      ...phase,
      filteredWeeks,
    };
  }).filter(Boolean);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Page Header */}
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-dark-700 pb-6">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <span className="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
              16 Weeks • 112 Days
            </span>
            <span className="text-xs font-mono text-dark-400">
              {overview?.completed_days} completed
            </span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-dark-100">
            Curriculum Explorer
          </h1>
          <p className="text-sm text-dark-400 mt-1">
            Every day is directly addressable. Choose any day to study conceptual deep-dives, run code exercises, and take quizzes.
          </p>
        </div>

        {/* Global Progress Pill */}
        <div className="flex items-center gap-4 bg-dark-900 border border-dark-700 rounded-xl p-3 shrink-0">
          <div>
            <div className="text-[11px] font-mono text-dark-400">Progress Tracker</div>
            <div className="text-lg font-bold font-mono text-emerald-400">
              {overview?.completed_days} / {overview?.total_days} Days
            </div>
          </div>
          <div className="w-16 h-2 bg-dark-800 rounded-full overflow-hidden">
            <div
              className="h-full bg-emerald-400"
              style={{
                width: `${((overview?.completed_days || 0) / (overview?.total_days || 112)) * 100}%`,
              }}
            />
          </div>
        </div>
      </div>

      {/* Filter & Search Bar */}
      <div className="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-4 gap-3 bg-dark-900 p-4 rounded-xl border border-dark-700">
        {/* Search */}
        <div className="sm:col-span-2 relative">
          <Search className="w-4 h-4 absolute left-3 top-3 text-dark-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search topics, concepts, frameworks..."
            className="w-full bg-dark-950 border border-dark-700 rounded-lg pl-9 pr-4 py-2 text-xs font-mono text-dark-100 placeholder-dark-500 focus:outline-none focus:border-emerald-500"
          />
        </div>

        {/* Phase Filter */}
        <div>
          <select
            value={selectedPhase}
            onChange={(e) =>
              setSelectedPhase(e.target.value === 'all' ? 'all' : Number(e.target.value))
            }
            className="w-full bg-dark-950 border border-dark-700 rounded-lg px-3 py-2 text-xs font-mono text-dark-200 focus:outline-none focus:border-emerald-500"
          >
            <option value="all">All Phases (1–4)</option>
            <option value="1">Phase 1: Foundations (Days 1–28)</option>
            <option value="2">Phase 2: React & Web (Days 29–70)</option>
            <option value="3">Phase 3: Async & DevOps (Days 71–98)</option>
            <option value="4">Phase 4: Capstone (Days 99–112)</option>
          </select>
        </div>

        {/* Status Filter */}
        <div>
          <select
            value={selectedStatus}
            onChange={(e) => setSelectedStatus(e.target.value)}
            className="w-full bg-dark-950 border border-dark-700 rounded-lg px-3 py-2 text-xs font-mono text-dark-200 focus:outline-none focus:border-emerald-500"
          >
            <option value="all">All Statuses</option>
            <option value="not_started">Not Started</option>
            <option value="in_progress">In Progress</option>
            <option value="completed">Completed</option>
          </select>
        </div>
      </div>

      {/* Curriculum Phases & Weeks Accordion */}
      <div className="space-y-8">
        {filteredPhases && filteredPhases.length > 0 ? (
          filteredPhases.map((phase) => {
            if (!phase) return null;
            return (
              <div key={phase.phase_number} className="space-y-4">
                {/* Phase Header */}
                <div className="flex items-center justify-between border-b border-dark-800 pb-2">
                  <div className="flex items-center gap-3">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-400" />
                    <h2 className="text-lg font-bold text-dark-100">{phase.title}</h2>
                    <span className="text-xs font-mono text-dark-400">
                      {phase.weeks_range} • {phase.days_range}
                    </span>
                  </div>
                  <span className="text-xs font-mono text-dark-500 hidden sm:block">
                    {phase.focus_area}
                  </span>
                </div>

                {/* Weeks in Phase */}
                <div className="space-y-3">
                  {phase.filteredWeeks.map((week) => {
                    const isExpanded = expandedWeeks[week.week_number] ?? false;

                    return (
                      <div
                        key={week.week_number}
                        className="rounded-xl bg-dark-900 border border-dark-700 overflow-hidden"
                      >
                        {/* Week Accordion Header */}
                        <div
                          onClick={() => toggleWeek(week.week_number)}
                          className="p-4 flex items-center justify-between cursor-pointer hover:bg-dark-850 transition-colors"
                        >
                          <div className="flex items-center gap-3">
                            <button className="text-dark-400 hover:text-dark-200">
                              {isExpanded ? (
                                <ChevronUp className="w-5 h-5" />
                              ) : (
                                <ChevronDown className="w-5 h-5" />
                              )}
                            </button>
                            <div>
                              <div className="flex items-center gap-2">
                                <span className="font-mono text-xs font-bold text-emerald-400">
                                  Week {week.week_number}
                                </span>
                                <span className="text-dark-500 font-mono text-xs">•</span>
                                <span className="font-mono text-xs text-dark-400">
                                  {week.days_range}
                                </span>
                              </div>
                              <h3 className="text-sm font-semibold text-dark-100 mt-0.5">
                                {week.title}
                              </h3>
                            </div>
                          </div>

                          <div className="flex items-center gap-3">
                            {/* Milestone Pill */}
                            <div className="hidden sm:flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-mono bg-dark-800 border border-dark-700 text-dark-300">
                              <Award className="w-3.5 h-3.5 text-emerald-400" />
                              <span className="truncate max-w-[180px]">{week.milestone_title}</span>
                            </div>

                            <span className="text-xs font-mono text-dark-500">
                              {week.filteredLessons.length} Lessons
                            </span>
                          </div>
                        </div>

                        {/* Lessons Grid (Expanded) */}
                        {isExpanded && (
                          <div className="p-4 pt-0 border-t border-dark-800/60 divide-y divide-dark-800/80">
                            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 pt-3">
                              {week.filteredLessons.map((lesson) => (
                                <Link
                                  key={lesson.id}
                                  to={`/curriculum/${lesson.day_number}`}
                                  className="p-3.5 rounded-lg bg-dark-950 border border-dark-800 hover:border-emerald-500/50 hover:bg-dark-900 transition-all flex flex-col justify-between group"
                                >
                                  <div>
                                    <div className="flex items-center justify-between gap-2 mb-2">
                                      <span className="px-2 py-0.5 text-[10px] font-mono rounded bg-dark-800 text-emerald-400 border border-dark-700">
                                        Day {lesson.day_number}
                                      </span>

                                      <div className="flex items-center gap-2">
                                        <button
                                          onClick={(e) => handleToggleBookmark(lesson.day_number, e)}
                                          className={`p-1 rounded transition-colors ${
                                            lesson.is_bookmarked
                                              ? 'text-amber-400'
                                              : 'text-dark-600 hover:text-dark-300'
                                          }`}
                                          title={lesson.is_bookmarked ? 'Bookmarked' : 'Add bookmark'}
                                        >
                                          <Bookmark className="w-3.5 h-3.5 fill-current" />
                                        </button>

                                        {lesson.status === 'completed' ? (
                                          <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                                        ) : lesson.status === 'in_progress' ? (
                                          <Clock className="w-4 h-4 text-amber-400" />
                                        ) : (
                                          <div className="w-3.5 h-3.5 rounded-full border border-dark-700" />
                                        )}
                                      </div>
                                    </div>

                                    <h4 className="text-xs font-semibold text-dark-100 group-hover:text-emerald-300 transition-colors line-clamp-2">
                                      {lesson.title}
                                    </h4>
                                    <p className="text-[11px] text-dark-400 line-clamp-2 mt-1">
                                      {lesson.summary}
                                    </p>
                                  </div>

                                  <div className="mt-3 pt-2 border-t border-dark-800/80 flex items-center justify-between text-[10px] font-mono text-dark-500">
                                    <span>{lesson.duration_minutes} mins</span>
                                    <span className="text-emerald-400 group-hover:translate-x-0.5 transition-transform flex items-center gap-1">
                                      Open <ArrowRight className="w-3 h-3" />
                                    </span>
                                  </div>
                                </Link>
                              ))}
                            </div>
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>
            );
          })
        ) : (
          <div className="p-12 text-center rounded-xl bg-dark-900 border border-dark-700 space-y-3">
            <BookOpen className="w-8 h-8 text-dark-500 mx-auto" />
            <h3 className="text-sm font-semibold text-dark-200">No lessons match your filter</h3>
            <p className="text-xs text-dark-400 font-mono">
              Try adjusting your search terms or clearing the status/phase filters.
            </p>
            <button
              onClick={() => {
                setSearchQuery('');
                setSelectedPhase('all');
                setSelectedStatus('all');
              }}
              className="px-3 py-1.5 text-xs font-mono rounded bg-dark-800 hover:bg-dark-700 text-dark-200"
            >
              Reset All Filters
            </button>
          </div>
        )}
      </div>
    </div>
  );
};
