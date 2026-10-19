import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Search, X, BookOpen, ChevronRight, CheckCircle2, Clock } from 'lucide-react';
import { api } from '../../api/client';
import { LessonSummaryOut } from '../../api/types';

interface SearchModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const SearchModal: React.FC<SearchModalProps> = ({ isOpen, onClose }) => {
  const navigate = useNavigate();
  const inputRef = useRef<HTMLInputElement>(null);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<LessonSummaryOut[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 50);
    } else {
      setQuery('');
      setResults([]);
    }
  }, [isOpen]);

  useEffect(() => {
    if (!isOpen) return;
    const timer = setTimeout(() => {
      setLoading(true);
      api.searchLessons(query)
        .then((res) => {
          setResults(res.slice(0, 15));
        })
        .catch(() => setResults([]))
        .finally(() => setLoading(false));
    }, 200);

    return () => clearTimeout(timer);
  }, [query, isOpen]);

  if (!isOpen) return null;

  const handleSelect = (dayNumber: number) => {
    onClose();
    navigate(`/curriculum/${dayNumber}`);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-16 px-4 bg-black/70 backdrop-blur-sm">
      <div
        className="w-full max-w-2xl bg-dark-900 border border-dark-700 rounded-xl shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-150"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Search Input Bar */}
        <div className="flex items-center px-4 py-3 border-b border-dark-700 gap-3">
          <Search className="w-5 h-5 text-emerald-400" />
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search concepts, frameworks, or day (e.g. FastAPI, Docker, Day 50)..."
            className="flex-1 bg-transparent text-dark-100 placeholder-dark-500 text-sm focus:outline-none"
          />
          {query && (
            <button onClick={() => setQuery('')} className="text-dark-500 hover:text-dark-300">
              <X className="w-4 h-4" />
            </button>
          )}
          <kbd
            onClick={onClose}
            className="px-2 py-0.5 text-xs font-mono bg-dark-800 border border-dark-700 rounded text-dark-400 cursor-pointer hover:bg-dark-700"
          >
            ESC
          </kbd>
        </div>

        {/* Results List */}
        <div className="max-h-[60vh] overflow-y-auto divide-y divide-dark-800">
          {loading ? (
            <div className="p-8 text-center text-dark-400 text-xs font-mono">
              Scanning 112 curriculum days...
            </div>
          ) : results.length > 0 ? (
            results.map((l) => (
              <div
                key={l.id}
                onClick={() => handleSelect(l.day_number)}
                className="p-3.5 hover:bg-dark-850 cursor-pointer flex items-center justify-between group transition-colors"
              >
                <div className="flex items-start gap-3">
                  <div className="px-2 py-1 rounded bg-dark-800 border border-dark-700 font-mono text-xs text-emerald-400 flex items-center gap-1.5 shrink-0">
                    <BookOpen className="w-3 h-3" />
                    <span>Day {l.day_number}</span>
                  </div>
                  <div>
                    <h4 className="text-sm font-medium text-dark-200 group-hover:text-emerald-300 transition-colors">
                      {l.title}
                    </h4>
                    <p className="text-xs text-dark-400 line-clamp-1 mt-0.5">{l.summary}</p>
                  </div>
                </div>

                <div className="flex items-center gap-2 shrink-0 ml-4">
                  {l.status === 'completed' && (
                    <span className="flex items-center gap-1 text-[11px] font-mono text-emerald-400">
                      <CheckCircle2 className="w-3.5 h-3.5" />
                      Done
                    </span>
                  )}
                  {l.status === 'in_progress' && (
                    <span className="flex items-center gap-1 text-[11px] font-mono text-amber-400">
                      <Clock className="w-3.5 h-3.5" />
                      Active
                    </span>
                  )}
                  <ChevronRight className="w-4 h-4 text-dark-600 group-hover:text-emerald-400 transition-colors" />
                </div>
              </div>
            ))
          ) : query ? (
            <div className="p-8 text-center text-dark-400 text-xs font-mono">
              No matching lessons found for "{query}".
            </div>
          ) : (
            <div className="p-8 text-center text-dark-500 text-xs font-mono">
              Type keywords like "SQL", "Decorators", "WebSockets", "FastAPI" or "Week 12"
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
