# NeuroMatrix Learning Academy — Developer Guide

This guide covers setting up, running, testing, and developing within the **NeuroMatrix Learning Academy** codebase.

---

## 1. Prerequisites

- **Python**: Python 3.11+ (Python 3.13 recommended)
- **Node.js**: Node.js 18+ (Node 20 recommended) with npm
- **Package Managers**: `uv` for high-speed Python management, `npm` for frontend packages
- **Operating System**: Linux / macOS / WSL2

---

## 2. Quickstart Execution

### One-Command Runner
The repository includes a root `start.sh` runner that prepares virtual environments, installs dependencies, builds static assets, and launches the application:

```bash
# Start Production Server (FastAPI serves API + React build on port 8000)
./start.sh

# Start Dual Hot-Reload Development Servers (FastAPI :8000 + Vite :5173)
./start.sh dev
```

Once running:
- **Web Application**: `http://localhost:8000` (or `http://localhost:5173` in dev mode)
- **Interactive OpenAPI Documentation**: `http://localhost:8000/docs`
- **ReDoc Alternative API Docs**: `http://localhost:8000/redoc`

---

## 3. Backend Development

The backend is organized as a modern FastAPI async service located in `backend/`:

```bash
cd backend

# Create virtual environment with uv
uv venv .venv
source .venv/bin/activate

# Install dependencies in editable mode
uv pip install -e ".[dev]"

# Run development server with live auto-reload
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### Database Management
- The SQLite database file is generated at `backend/neuromatrix_academy.db`.
- On application boot, the FastAPI `lifespan` hook automatically calls `init_db()` to create missing tables and `seed_curriculum()` to populate all 16 weeks and 112 days idempotently.
- To re-seed or reset database from scratch:
  ```bash
  rm backend/neuromatrix_academy.db
  # Restart the server; database and curriculum will reseed automatically
  ```

### Code Quality & Formatting
We enforce strict linting and formatting standards using Ruff:

```bash
# Run linter checks
backend/.venv/bin/ruff check app tests

# Run auto-fixes
backend/.venv/bin/ruff check app tests --fix

# Format code
backend/.venv/bin/ruff format app tests
```

---

## 4. Frontend Development

The frontend is a React 18 single-page application built with Vite and Tailwind CSS:

```bash
cd frontend

# Install dependencies
npm install

# Start Vite dev server with proxy to backend
npm run dev

# Run TypeScript compiler checks and production build
npm run build

# Preview production build locally
npm run preview
```

### Styling Guidelines
- Maintain the **cybersecurity-inspired aesthetic**:
  - Dark surfaces: `bg-dark-950` (`#07090b`), `bg-dark-900` (`#0d1117`), `bg-dark-850` (`#11161f`)
  - Subtle borders: `border-dark-700` (`#21262d`), `border-dark-800` (`#161b22`)
  - Restrained accents: `text-emerald-400` (`#10b981`), `text-cyan-400` (`#06b6d4`), `text-amber-400` (`#f59e0b`)
  - Monospace elements: code snippets, status tags, and metrics must use `font-mono` (`JetBrains Mono`).

---

## 5. Adding New Curriculum Content

Curriculum days are defined in structured modules under `backend/app/services/curriculum_data/`:
- `phases_and_weeks.py`: High-level phases and weekly milestone metadata
- `days_phase1.py`: Days 1–28 (Python Fundamentals & Engineering)
- `days_phase2.py`: Days 29–70 (JavaScript, React, Databases, FastAPI, Security, Integration)
- `days_phase3.py`: Days 71–98 (Asyncio, WebSockets, Testing, Docker, Mobile)
- `days_phase4.py`: Days 99–112 (Observability, Caching, Capstone Release)

Every day dictionary requires:
- `title`, `slug`, `summary`, `duration_minutes`
- `objectives`, `prerequisites`, `revision_questions`
- `concept_sections` (title, content, key_points)
- `code_examples` (title, description, code, language, expected_output)
- `exercises` (id, title, difficulty, instructions, starter_code, solution_code, expected_output, acceptance_criteria, test_cases)
- `common_errors` (error_type, cause, fix, example)
- `edge_cases` (list of strings)
- `neuromatrix_integration` (topic, context, task_description, target_component, verification_step)
- `completion_criteria` (list of strings)
- `quiz_questions` (id, question_text, question_type, code_snippet, options, correct_answer, explanation)
