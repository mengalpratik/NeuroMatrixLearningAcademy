# NeuroMatrix Learning Academy

[![Python](https://img.shields.io/badge/Python-3.13-10b981?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-059669?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18.3-06b6d4?style=flat-square&logo=react&logoColor=white)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.4-3b82f6?style=flat-square&logo=typescript&logoColor=white)](https://typescriptlang.org)
[![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-3.4-10b981?style=flat-square&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![Tests](https://img.shields.io/badge/Tests-12%20Passed-10b981?style=flat-square)](docs/TESTING.md)

A professional, full-stack learning platform designed to organize, deliver, and track a **112-day Python full-stack engineering roadmap**. Built with a cybersecurity-inspired dark design system, the academy allows learners to jump directly to any day, study deep conceptual explanations, run code exercises, take quizzes, complete milestone engineering projects, and persist all progress across application restarts.

---

## Key Features

- **Dashboard Telemetry**: Displays real persisted metrics (current day, completed lessons, active in-progress studies, overall completion percentage, weekly milestone status, and live activity streams).
- **Direct 112-Day Addressability**: Open any day directly via URL (`/curriculum/1` through `/curriculum/112`) without scrolling through previous lessons.
- **Curriculum Explorer**: Week-by-week accordion view covering all 16 weeks and 112 days with search, phase filtering, and status filtering.
- **Rich Lesson Workspace**:
  - Structured learning objectives, prerequisites, and revision questions.
  - Deep conceptual breakdowns with key takeaways.
  - Copyable runnable code blocks with verified expected outputs.
  - Practical hands-on exercises with acceptance criteria, test cases, and an in-browser output recorder.
  - Reference solution reveal toggles.
  - Common pitfalls, root cause analysis, and edge cases.
  - Interactive knowledge quizzes with instant evaluation and detailed explanations.
  - Practical NeuroMatrix engineering integration tasks.
  - In-page persistent study notes editor and bookmark pinning.
  - Sequential previous and next day navigation.
- **Practice Lab**: Drill question bank filterable by week and category (Multiple Choice, Code Reading, Output Prediction, Debugging Challenges) with instant answer verification and scoring history.
- **NeuroMatrix Project Lab**: Connects lessons to practical engineering deliverables across 16 weekly milestones (from CLI tools in Week 1 to the production Capstone in Week 16). Track implementation notes, Git commit hashes, PR links, and test verification results.
- **Study Notes & Bookmarks**: Central repository of all saved lesson notes and bookmarked revision days.
- **Global Search Modal**: Quick-jump search activated anywhere via `Cmd+K` or `/`.

---

## System Architecture

```
NeuroMatrixAcademy/
├── backend/
│   ├── app/
│   │   ├── api/             # Modular API routes (curriculum, progress, quiz, notes, projects)
│   │   ├── core/            # Configuration, database engine, session makers
│   │   ├── models/          # SQLAlchemy 2.0 declarative models
│   │   ├── schemas/         # Pydantic v2 validation schemas
│   │   ├── services/        # 112-day seed generator, progress logic, search engine
│   │   └── main.py          # FastAPI application factory, CORS, SPA fallback
│   ├── tests/               # Pytest async test suite (12/12 passing)
│   └── pyproject.toml       # Python dependencies & Ruff linter settings
├── frontend/
│   ├── src/
│   │   ├── api/             # Type-safe Fetch API client & TypeScript interfaces
│   │   ├── components/      # Navbar, Footer, SearchModal
│   │   ├── pages/           # Dashboard, Curriculum, Lesson, PracticeLab, ProjectLab, Notes
│   │   ├── styles/          # Tailwind styling & dark cybersecurity tokens
│   │   ├── App.tsx          # Client-side router & global keybindings
│   │   └── main.tsx         # React DOM entrypoint
│   └── vite.config.ts       # Vite bundler & API proxy configuration
├── docs/                    # Architecture, Curriculum, Dev Guide, and Testing docs
├── start.sh                 # Unified launch runner script
└── README.md
```

---

## Getting Started

### 1. Launch with One Command

```bash
# Clone or navigate to the repository
cd /home/neuro/Projects/NeuroMatrixAcademy

# Production Mode (Starts unified FastAPI server on port 8000)
./start.sh
```

Open your browser to:
- **Application UI**: [http://localhost:8000](http://localhost:8000)
- **Interactive OpenAPI Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

### 2. Development Mode (Dual Hot-Reload)

```bash
./start.sh dev
```
- **Vite Client**: [http://localhost:5173](http://localhost:5173)
- **FastAPI API**: [http://localhost:8000](http://localhost:8000)

### 3. Docker Deployment

To build and run the containerized production stack using Docker and Docker Compose:

```bash
# Copy example environment configuration
cp .env.example .env

# Build and start container (binds to port 18080 by default, customizable via ACADEMY_HOST_PORT)
docker compose up -d --build

# Verify container health and status
docker compose ps
curl http://localhost:18080/api/health
```

---

## Running Quality Checks & Tests

### Backend Test Suite
```bash
cd backend
.venv/bin/pytest -v
```

### Python Code Quality & Linting
```bash
cd backend
.venv/bin/ruff check app tests
.venv/bin/ruff format --check app tests
```

### Frontend Type Checking & Build
```bash
cd frontend
npm run build
```

---

## 112-Day Curriculum Summary

| Phase | Weeks | Days | Focus Area |
| :--- | :--- | :--- | :--- |
| **Phase 1** | Weeks 1–4 | Days 1–28 | Python setup, primitives, control flow, functions, OOP, exceptions, file I/O, Linux terminal, HTTP, and static dashboard. |
| **Phase 2** | Weeks 5–10 | Days 29–70 | Modern JavaScript, React architecture, relational databases & SQL, FastAPI REST endpoints, security, and full-stack integration. |
| **Phase 3** | Weeks 11–14 | Days 71–98 | Asyncio event loops, WebSockets, real-time heartbeats, automated Pytest suites, Docker containerization, and React Native mobile companion. |
| **Phase 4** | Weeks 15–16 | Days 99–112 | Structured logging, Prometheus observability, Redis caching, system design, codebase audit, and final Capstone release. |

Detailed syllabus: [docs/CURRICULUM.md](docs/CURRICULUM.md).

---

## Documentation

- [Architecture Specification](docs/ACADEMY_ARCHITECTURE.md)
- [Complete Curriculum Reference](docs/CURRICULUM.md)
- [Developer Guide](docs/DEVELOPMENT_GUIDE.md)
- [Testing & Quality Assurance Guide](docs/TESTING.md)
- [Project Progress & Verification Log](PROJECT_PROGRESS.md)

---

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

Copyright (c) 2026 Pratik Mengal.

