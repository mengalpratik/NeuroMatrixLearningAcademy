import React, { useEffect, useState } from 'react';
import {
  Shield,
  GitCommit,
  ExternalLink,
  Edit3,
  Save,
  X,
  Check,
} from 'lucide-react';
import { api } from '../api/client';
import { ProjectTaskOut, ProjectTaskUpdate } from '../api/types';

export const ProjectLabPage: React.FC = () => {
  const [tasks, setTasks] = useState<ProjectTaskOut[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTask, setActiveTask] = useState<ProjectTaskOut | null>(null);

  // Form edit state
  const [editStatus, setEditStatus] = useState<ProjectTaskOut['status']>('not_started');
  const [editNotes, setEditNotes] = useState('');
  const [editCommit, setEditCommit] = useState('');
  const [editPr, setEditPr] = useState('');
  const [editTestResults, setEditTestResults] = useState('');
  const [editIssues, setEditIssues] = useState('');
  const [saving, setSaving] = useState(false);
  const [saveSuccess, setSaveSuccess] = useState(false);

  const loadTasks = () => {
    setLoading(true);
    api.getProjectTasks()
      .then((data) => setTasks(data))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const openEditModal = (task: ProjectTaskOut) => {
    setActiveTask(task);
    setEditStatus(task.status);
    setEditNotes(task.implementation_notes || '');
    setEditCommit(task.git_commit_ref || '');
    setEditPr(task.pr_url || '');
    setEditTestResults(task.test_results || '');
    setEditIssues(task.remaining_issues || '');
    setSaveSuccess(false);
  };

  const handleSave = async () => {
    if (!activeTask) return;
    setSaving(true);
    try {
      const payload: ProjectTaskUpdate = {
        status: editStatus,
        implementation_notes: editNotes,
        git_commit_ref: editCommit,
        pr_url: editPr,
        test_results: editTestResults,
        remaining_issues: editIssues,
      };
      await api.updateProjectTask(activeTask.id, payload);
      setSaveSuccess(true);
      setTimeout(() => {
        setSaveSuccess(false);
        setActiveTask(null);
        loadTasks();
      }, 1000);
    } catch (err: any) {
      alert(`Save error: ${err.message}`);
    } finally {
      setSaving(false);
    }
  };

  const completedCount = tasks.filter((t) => t.status === 'completed' || t.status === 'verified').length;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-dark-700 pb-6">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <span className="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
              16 Engineering Milestones
            </span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-dark-100 flex items-center gap-3">
            <Shield className="w-7 h-7 text-emerald-400" />
            <span>NeuroMatrix Project Lab</span>
          </h1>
          <p className="text-sm text-dark-400 mt-1">
            Connect curriculum days to practical engineering deliverables. Record your Git commits, PRs, test evidence, and release notes.
          </p>
        </div>

        {/* Milestone Progress Pill */}
        <div className="bg-dark-900 border border-dark-700 rounded-xl p-3 shrink-0">
          <div className="text-[11px] font-mono text-dark-400">Milestones Verified</div>
          <div className="text-base font-bold font-mono text-emerald-400">
            {completedCount} / {tasks.length} Completed
          </div>
        </div>
      </div>

      {/* Project Tasks Grid */}
      {loading ? (
        <div className="py-16 text-center">
          <div className="w-8 h-8 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <span className="font-mono text-xs text-dark-400">Loading project lab milestones...</span>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {tasks.map((task) => (
            <div
              key={task.id}
              className="p-5 rounded-xl bg-dark-900 border border-dark-700 hover:border-dark-600 transition-all flex flex-col justify-between space-y-4"
            >
              <div className="space-y-2">
                <div className="flex items-center justify-between gap-2">
                  <div className="flex items-center gap-2">
                    <span className="px-2 py-0.5 text-[10px] font-mono rounded bg-dark-800 text-emerald-400 border border-dark-700">
                      Week {task.week_number}
                    </span>
                    <span className="text-xs font-mono text-dark-400">
                      Linked Day {task.linked_day_number}
                    </span>
                  </div>

                  <span
                    className={`px-2 py-0.5 text-[10px] font-mono rounded ${
                      task.status === 'verified'
                        ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30'
                        : task.status === 'completed'
                        ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
                        : task.status === 'in_progress'
                        ? 'bg-amber-500/10 text-amber-400 border border-amber-500/20'
                        : 'bg-dark-800 text-dark-500'
                    }`}
                  >
                    {task.status.replace('_', ' ')}
                  </span>
                </div>

                <h3 className="text-sm font-bold text-dark-100">{task.title}</h3>
                <p className="text-xs text-dark-300 line-clamp-2 leading-relaxed">
                  {task.description}
                </p>

                {/* Git commit & PR pills */}
                {(task.git_commit_ref || task.pr_url) && (
                  <div className="flex flex-wrap gap-2 pt-1">
                    {task.git_commit_ref && (
                      <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-mono bg-dark-950 border border-dark-800 text-dark-300">
                        <GitCommit className="w-3 h-3 text-emerald-400" />
                        {task.git_commit_ref}
                      </span>
                    )}
                    {task.pr_url && (
                      <a
                        href={task.pr_url}
                        target="_blank"
                        rel="noreferrer"
                        className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-mono bg-dark-950 border border-dark-800 text-cyan-400 hover:underline"
                      >
                        <ExternalLink className="w-3 h-3" />
                        Pull Request
                      </a>
                    )}
                  </div>
                )}
              </div>

              <div className="pt-3 border-t border-dark-800 flex items-center justify-between">
                <span className="text-[11px] font-mono text-dark-500">
                  Updated {new Date(task.updated_at).toLocaleDateString()}
                </span>
                <button
                  onClick={() => openEditModal(task)}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-dark-800 hover:bg-dark-700 text-dark-200 text-xs font-mono transition-colors"
                >
                  <Edit3 className="w-3.5 h-3.5" />
                  <span>Update Artifacts</span>
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Edit Milestone Modal */}
      {activeTask && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-sm">
          <div className="w-full max-w-2xl bg-dark-900 border border-dark-700 rounded-xl shadow-2xl p-6 space-y-5 animate-in fade-in zoom-in-95">
            <div className="flex items-center justify-between border-b border-dark-800 pb-3">
              <div>
                <span className="text-xs font-mono text-emerald-400">
                  Week {activeTask.week_number} Milestone
                </span>
                <h3 className="text-base font-bold text-dark-100">{activeTask.title}</h3>
              </div>
              <button
                onClick={() => setActiveTask(null)}
                className="p-1 rounded text-dark-400 hover:text-dark-200"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="space-y-4 max-h-[70vh] overflow-y-auto pr-1">
              {/* Status */}
              <div>
                <label className="block text-xs font-mono text-dark-300 mb-1">
                  Milestone Status:
                </label>
                <select
                  value={editStatus}
                  onChange={(e) => setEditStatus(e.target.value as any)}
                  className="w-full bg-dark-950 border border-dark-700 rounded-lg px-3 py-2 text-xs font-mono text-dark-200 focus:outline-none focus:border-emerald-500"
                >
                  <option value="not_started">Not Started</option>
                  <option value="in_progress">In Progress</option>
                  <option value="completed">Completed</option>
                  <option value="verified">Verified</option>
                </select>
              </div>

              {/* Implementation Notes */}
              <div>
                <label className="block text-xs font-mono text-dark-300 mb-1">
                  Implementation Notes:
                </label>
                <textarea
                  rows={3}
                  value={editNotes}
                  onChange={(e) => setEditNotes(e.target.value)}
                  placeholder="Describe your architecture decisions, files created, and patterns applied..."
                  className="w-full bg-dark-950 border border-dark-700 rounded-lg p-3 text-xs font-mono text-dark-200 placeholder-dark-600 focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* Git Commit & PR */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-mono text-dark-300 mb-1">
                    Git Commit Reference:
                  </label>
                  <input
                    type="text"
                    value={editCommit}
                    onChange={(e) => setEditCommit(e.target.value)}
                    placeholder="e.g. commit 4a8b79f or git tag v1.0"
                    className="w-full bg-dark-950 border border-dark-700 rounded-lg px-3 py-2 text-xs font-mono text-dark-200 placeholder-dark-600 focus:outline-none focus:border-emerald-500"
                  />
                </div>
                <div>
                  <label className="block text-xs font-mono text-dark-300 mb-1">
                    Pull Request URL (optional):
                  </label>
                  <input
                    type="text"
                    value={editPr}
                    onChange={(e) => setEditPr(e.target.value)}
                    placeholder="https://github.com/.../pull/1"
                    className="w-full bg-dark-950 border border-dark-700 rounded-lg px-3 py-2 text-xs font-mono text-dark-200 placeholder-dark-600 focus:outline-none focus:border-emerald-500"
                  />
                </div>
              </div>

              {/* Test Results */}
              <div>
                <label className="block text-xs font-mono text-dark-300 mb-1">
                  Test Results & Verification Output:
                </label>
                <textarea
                  rows={3}
                  value={editTestResults}
                  onChange={(e) => setEditTestResults(e.target.value)}
                  placeholder="Paste pytest or CLI execution outputs proving acceptance criteria..."
                  className="w-full bg-dark-950 border border-dark-700 rounded-lg p-3 text-xs font-mono text-dark-200 placeholder-dark-600 focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* Remaining Issues */}
              <div>
                <label className="block text-xs font-mono text-dark-300 mb-1">
                  Remaining Issues / Technical Debt:
                </label>
                <input
                  type="text"
                  value={editIssues}
                  onChange={(e) => setEditIssues(e.target.value)}
                  placeholder="Note any edge cases or future optimizations..."
                  className="w-full bg-dark-950 border border-dark-700 rounded-lg px-3 py-2 text-xs font-mono text-dark-200 placeholder-dark-600 focus:outline-none focus:border-emerald-500"
                />
              </div>
            </div>

            <div className="flex items-center justify-between border-t border-dark-800 pt-4">
              {saveSuccess ? (
                <span className="flex items-center gap-1.5 text-xs font-mono text-emerald-400">
                  <Check className="w-4 h-4" /> Milestone Updated!
                </span>
              ) : (
                <div />
              )}
              <div className="flex items-center gap-3">
                <button
                  onClick={() => setActiveTask(null)}
                  className="px-4 py-2 rounded-lg bg-dark-800 hover:bg-dark-700 text-xs font-mono text-dark-300"
                >
                  Cancel
                </button>
                <button
                  onClick={handleSave}
                  disabled={saving}
                  className="px-5 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-600 text-black font-semibold text-xs font-mono transition-all flex items-center gap-2"
                >
                  <Save className="w-3.5 h-3.5" />
                  <span>{saving ? 'Saving...' : 'Save Milestone'}</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
