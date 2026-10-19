import React from 'react';
import { Shield, GitBranch, Cpu, Database } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="border-t border-dark-700 bg-dark-950 mt-16 py-8 text-xs text-dark-400">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="flex items-center gap-2">
          <Shield className="w-4 h-4 text-emerald-400" />
          <span className="font-mono text-dark-300 font-medium">NeuroMatrix Learning Academy</span>
          <span className="text-dark-600">|</span>
          <span className="font-mono text-[11px] text-dark-500">v1.0.0 Architecture</span>
        </div>

        <div className="flex items-center gap-6 font-mono text-[11px]">
          <span className="flex items-center gap-1.5 text-dark-400">
            <Cpu className="w-3.5 h-3.5 text-emerald-500" />
            FastAPI + Python 3.13
          </span>
          <span className="flex items-center gap-1.5 text-dark-400">
            <Database className="w-3.5 h-3.5 text-cyan-500" />
            SQLite / PostgreSQL
          </span>
          <span className="flex items-center gap-1.5 text-dark-400">
            <GitBranch className="w-3.5 h-3.5 text-emerald-400" />
            112-Day Continuous Track
          </span>
        </div>
      </div>
    </footer>
  );
};
