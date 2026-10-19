import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Navbar } from './components/common/Navbar';
import { Footer } from './components/common/Footer';
import { SearchModal } from './components/common/SearchModal';
import { DashboardPage } from './pages/DashboardPage';
import { CurriculumPage } from './pages/CurriculumPage';
import { LessonPage } from './pages/LessonPage';
import { PracticeLabPage } from './pages/PracticeLabPage';
import { ProjectLabPage } from './pages/ProjectLabPage';
import { NotesBookmarksPage } from './pages/NotesBookmarksPage';

export const App: React.FC = () => {
  const [searchOpen, setSearchOpen] = useState(false);

  // Global keyboard shortcuts: Cmd+K or '/' to open search
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setSearchOpen((prev) => !prev);
      } else if (e.key === '/' && (e.target as HTMLElement)?.tagName !== 'INPUT' && (e.target as HTMLElement)?.tagName !== 'TEXTAREA') {
        e.preventDefault();
        setSearchOpen(true);
      } else if (e.key === 'Escape') {
        setSearchOpen(false);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <BrowserRouter>
      <div className="flex flex-col min-h-screen bg-dark-950 text-dark-200">
        <Navbar onOpenSearch={() => setSearchOpen(true)} />

        <main className="flex-1">
          <Routes>
            <Route path="/" element={<DashboardPage />} />
            <Route path="/curriculum" element={<CurriculumPage />} />
            <Route path="/curriculum/:day" element={<LessonPage />} />
            <Route path="/lessons/:day" element={<LessonPage />} />
            <Route path="/practice" element={<PracticeLabPage />} />
            <Route path="/projects" element={<ProjectLabPage />} />
            <Route path="/notes" element={<NotesBookmarksPage />} />
            {/* 404 Fallback */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>

        <Footer />
        <SearchModal isOpen={searchOpen} onClose={() => setSearchOpen(false)} />
      </div>
    </BrowserRouter>
  );
};

export default App;
