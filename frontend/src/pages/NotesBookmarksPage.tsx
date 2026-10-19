import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import {
  Bookmark,
  FileText,
  Search,
  Trash2,
  ExternalLink,
  ChevronRight,
} from 'lucide-react';
import { api } from '../api/client';
import { BookmarkOut, LearningNoteOut } from '../api/types';

export const NotesBookmarksPage: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'bookmarks' | 'notes'>('bookmarks');
  const [bookmarks, setBookmarks] = useState<BookmarkOut[]>([]);
  const [notes, setNotes] = useState<LearningNoteOut[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');

  const loadData = () => {
    setLoading(true);
    Promise.all([api.getBookmarks(), api.getNotes()])
      .then(([bmData, notesData]) => {
        setBookmarks(bmData);
        setNotes(notesData);
      })
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleRemoveBookmark = async (dayNumber: number) => {
    try {
      await api.toggleBookmark(dayNumber);
      setBookmarks((prev) => prev.filter((b) => b.day_number !== dayNumber));
    } catch (err) {
      console.error(err);
    }
  };

  const handleDeleteNote = async (noteId: number) => {
    if (!window.confirm('Are you sure you want to delete this study note?')) return;
    try {
      await api.deleteNote(noteId);
      setNotes((prev) => prev.filter((n) => n.id !== noteId));
    } catch (err) {
      console.error(err);
    }
  };

  const filteredBookmarks = bookmarks.filter((b) => {
    if (!searchQuery.trim()) return true;
    const q = searchQuery.toLowerCase();
    return (
      (b.lesson_title && b.lesson_title.toLowerCase().includes(q)) ||
      `day ${b.day_number}`.includes(q)
    );
  });

  const filteredNotes = notes.filter((n) => {
    if (!searchQuery.trim()) return true;
    const q = searchQuery.toLowerCase();
    return (
      n.title.toLowerCase().includes(q) ||
      n.content.toLowerCase().includes(q) ||
      `day ${n.day_number}`.includes(q)
    );
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-dark-700 pb-6">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <span className="px-2 py-0.5 rounded text-[11px] font-mono bg-amber-500/10 text-amber-400 border border-amber-500/30">
              Personal Knowledge Base
            </span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-dark-100 flex items-center gap-3">
            <Bookmark className="w-7 h-7 text-amber-400" />
            <span>Notes & Bookmarks</span>
          </h1>
          <p className="text-sm text-dark-400 mt-1">
            Access your saved revision days and comprehensive engineering study notes.
          </p>
        </div>

        {/* Tab switchers */}
        <div className="flex items-center rounded-xl bg-dark-900 border border-dark-700 p-1 text-xs font-mono">
          <button
            onClick={() => setActiveTab('bookmarks')}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
              activeTab === 'bookmarks'
                ? 'bg-amber-500/10 text-amber-400 border border-amber-500/30 font-semibold'
                : 'text-dark-400 hover:text-dark-200'
            }`}
          >
            <Bookmark className="w-4 h-4" />
            <span>Bookmarks ({bookmarks.length})</span>
          </button>
          <button
            onClick={() => setActiveTab('notes')}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
              activeTab === 'notes'
                ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 font-semibold'
                : 'text-dark-400 hover:text-dark-200'
            }`}
          >
            <FileText className="w-4 h-4" />
            <span>Study Notes ({notes.length})</span>
          </button>
        </div>
      </div>

      {/* Search Input */}
      <div className="relative max-w-md">
        <Search className="w-4 h-4 absolute left-3 top-3 text-dark-400" />
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder={`Search ${activeTab}...`}
          className="w-full bg-dark-900 border border-dark-700 rounded-lg pl-9 pr-4 py-2 text-xs font-mono text-dark-100 placeholder-dark-500 focus:outline-none focus:border-emerald-500"
        />
      </div>

      {/* Content */}
      {loading ? (
        <div className="py-16 text-center">
          <div className="w-8 h-8 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <span className="font-mono text-xs text-dark-400">Loading saved items...</span>
        </div>
      ) : activeTab === 'bookmarks' ? (
        filteredBookmarks.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {filteredBookmarks.map((bm) => (
              <div
                key={bm.id}
                className="p-5 rounded-xl bg-dark-900 border border-dark-700 hover:border-dark-600 transition-all flex flex-col justify-between space-y-3"
              >
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="px-2 py-0.5 text-[10px] font-mono rounded bg-dark-800 text-amber-400 border border-dark-700">
                      Day {bm.day_number}
                    </span>
                    <button
                      onClick={() => handleRemoveBookmark(bm.day_number)}
                      className="text-dark-500 hover:text-red-400 p-1"
                      title="Remove bookmark"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>

                  <h3 className="text-sm font-semibold text-dark-100 line-clamp-2">
                    {bm.lesson_title || `Day ${bm.day_number} Lesson`}
                  </h3>
                  <div className="text-[10px] font-mono text-dark-500 mt-1">
                    Bookmarked {new Date(bm.created_at).toLocaleDateString()}
                  </div>
                </div>

                <div className="pt-3 border-t border-dark-800 flex items-center justify-end">
                  <Link
                    to={`/curriculum/${bm.day_number}`}
                    className="flex items-center gap-1 text-xs font-mono text-emerald-400 hover:underline"
                  >
                    <span>Open Workspace</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </Link>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="p-12 text-center rounded-xl bg-dark-900 border border-dark-700 space-y-2">
            <Bookmark className="w-8 h-8 text-dark-500 mx-auto" />
            <h3 className="text-sm font-semibold text-dark-200">No bookmarks saved yet</h3>
            <p className="text-xs font-mono text-dark-400">
              Click the bookmark icon on any lesson card to pin days for quick revision.
            </p>
          </div>
        )
      ) : filteredNotes.length > 0 ? (
        <div className="space-y-4">
          {filteredNotes.map((note) => (
            <div
              key={note.id}
              className="p-6 rounded-xl bg-dark-900 border border-dark-700 space-y-3"
            >
              <div className="flex items-center justify-between gap-4">
                <div className="flex items-center gap-2">
                  <span className="px-2 py-0.5 text-[10px] font-mono rounded bg-dark-800 text-emerald-400 border border-dark-700">
                    Day {note.day_number}
                  </span>
                  <h3 className="text-sm font-bold text-dark-100">{note.title}</h3>
                </div>

                <div className="flex items-center gap-2">
                  <Link
                    to={`/curriculum/${note.day_number}`}
                    className="p-1.5 rounded text-dark-400 hover:text-emerald-400 text-xs font-mono flex items-center gap-1"
                    title="View Day"
                  >
                    <ExternalLink className="w-3.5 h-3.5" />
                  </Link>
                  <button
                    onClick={() => handleDeleteNote(note.id)}
                    className="p-1.5 rounded text-dark-500 hover:text-red-400"
                    title="Delete note"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>

              <div className="p-4 rounded-lg bg-dark-950 border border-dark-800 text-xs text-dark-200 font-mono whitespace-pre-wrap leading-relaxed">
                {note.content}
              </div>

              <div className="text-[10px] font-mono text-dark-500 text-right">
                Last updated {new Date(note.updated_at).toLocaleString()}
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="p-12 text-center rounded-xl bg-dark-900 border border-dark-700 space-y-2">
          <FileText className="w-8 h-8 text-dark-500 mx-auto" />
          <h3 className="text-sm font-semibold text-dark-200">No study notes recorded yet</h3>
          <p className="text-xs font-mono text-dark-400">
            Open any lesson workspace and save personal notes in the "Study Notes" tab.
          </p>
        </div>
      )}
    </div>
  );
};
