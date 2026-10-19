import React, { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import {
  Shield,
  BookOpen,
  Terminal,
  Cpu,
  Bookmark,
  Search,
  Menu,
  X,
  ChevronRight,
} from 'lucide-react';
import { api } from '../../api/client';

interface NavbarProps {
  onOpenSearch: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({ onOpenSearch }) => {
  const location = useLocation();
  const navigate = useNavigate();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [apiHealthy, setApiHealthy] = useState<boolean | null>(null);
  const [selectedJumpDay, setSelectedJumpDay] = useState<string>('');

  useEffect(() => {
    let mounted = true;
    api.checkHealth()
      .then((res) => {
        if (mounted) setApiHealthy(res.status === 'healthy');
      })
      .catch(() => {
        if (mounted) setApiHealthy(false);
      });
    return () => {
      mounted = false;
    };
  }, []);

  const navLinks = [
    { name: 'Dashboard', path: '/', icon: Cpu },
    { name: 'Curriculum', path: '/curriculum', icon: BookOpen },
    { name: 'Practice Lab', path: '/practice', icon: Terminal },
    { name: 'Project Lab', path: '/projects', icon: Shield },
    { name: 'Notes & Bookmarks', path: '/notes', icon: Bookmark },
  ];

  const handleJump = (day: string) => {
    if (!day) return;
    setSelectedJumpDay(day);
    navigate(`/curriculum/${day}`);
  };

  return (
    <header className="sticky top-0 z-40 w-full border-b border-dark-700 bg-dark-950/80 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand */}
        <div className="flex items-center gap-6">
          <Link to="/" className="flex items-center gap-3 group">
            <div className="w-9 h-9 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 group-hover:border-emerald-500/60 group-hover:bg-emerald-500/20 transition-all">
              <Shield className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-mono text-sm font-bold tracking-wider text-dark-100">
                  NEUROMATRIX
                </span>
                <span className="px-1.5 py-0.5 text-[10px] font-mono uppercase tracking-widest bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 rounded">
                  Academy
                </span>
              </div>
              <div className="text-[11px] text-dark-400 font-mono hidden sm:block">
                112-Day Python Full-Stack Journey
              </div>
            </div>
          </Link>

          {/* Quick Day Jump */}
          <div className="hidden lg:flex items-center gap-2 pl-4 border-l border-dark-700">
            <span className="text-xs text-dark-400 font-mono">Day:</span>
            <select
              value={selectedJumpDay}
              onChange={(e) => handleJump(e.target.value)}
              className="bg-dark-900 border border-dark-700 text-dark-200 text-xs font-mono rounded px-2 py-1 focus:outline-none focus:border-emerald-500"
            >
              <option value="">Jump to Day...</option>
              {Array.from({ length: 112 }, (_, i) => i + 1).map((d) => (
                <option key={d} value={d}>
                  Day {d}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Desktop Navigation */}
        <nav className="hidden md:flex items-center gap-1">
          {navLinks.map((link) => {
            const Icon = link.icon;
            const isActive =
              link.path === '/'
                ? location.pathname === '/'
                : location.pathname.startsWith(link.path);

            return (
              <Link
                key={link.path}
                to={link.path}
                className={`flex items-center gap-2 px-3 py-1.5 rounded-md text-xs font-medium transition-all ${
                  isActive
                    ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30'
                    : 'text-dark-300 hover:text-dark-100 hover:bg-dark-800'
                }`}
              >
                <Icon className="w-4 h-4" />
                <span>{link.name}</span>
              </Link>
            );
          })}
        </nav>

        {/* Action Controls & Health */}
        <div className="flex items-center gap-3">
          {/* Global Search Button */}
          <button
            onClick={onOpenSearch}
            className="flex items-center gap-2 px-2.5 py-1.5 rounded-md bg-dark-900 border border-dark-700 hover:border-dark-600 text-dark-400 hover:text-dark-200 text-xs transition-colors"
            title="Search curriculum (Cmd+K)"
          >
            <Search className="w-3.5 h-3.5 text-emerald-400" />
            <span className="hidden sm:inline font-mono">Search</span>
            <kbd className="hidden sm:inline-block px-1.5 py-0.5 text-[10px] bg-dark-800 border border-dark-700 rounded text-dark-400 font-mono">
              /
            </kbd>
          </button>

          {/* System Status Pill */}
          <div
            className="hidden sm:flex items-center gap-1.5 px-2 py-1 rounded-full text-[11px] font-mono border border-dark-700 bg-dark-900"
            title={apiHealthy ? 'API Service Operational' : 'Connecting to API...'}
          >
            {apiHealthy ? (
              <>
                <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                <span className="text-emerald-400">Node Ready</span>
              </>
            ) : (
              <>
                <div className="w-2 h-2 rounded-full bg-amber-400" />
                <span className="text-amber-400">Connecting</span>
              </>
            )}
          </div>

          {/* Mobile menu button */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="md:hidden p-2 rounded text-dark-400 hover:text-dark-100 hover:bg-dark-800"
          >
            {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && (
        <div className="md:hidden border-b border-dark-700 bg-dark-900 px-4 pt-2 pb-4 space-y-1">
          {navLinks.map((link) => {
            const Icon = link.icon;
            const isActive =
              link.path === '/'
                ? location.pathname === '/'
                : location.pathname.startsWith(link.path);

            return (
              <Link
                key={link.path}
                to={link.path}
                onClick={() => setMobileMenuOpen(false)}
                className={`flex items-center justify-between px-3 py-2 rounded-md text-sm font-medium ${
                  isActive
                    ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
                    : 'text-dark-300 hover:bg-dark-800'
                }`}
              >
                <div className="flex items-center gap-3">
                  <Icon className="w-4 h-4" />
                  <span>{link.name}</span>
                </div>
                <ChevronRight className="w-4 h-4 text-dark-500" />
              </Link>
            );
          })}
        </div>
      )}
    </header>
  );
};
