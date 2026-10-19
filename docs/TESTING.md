# NeuroMatrix Learning Academy — Testing & Quality Assurance Guide

This document details the automated test suites, quality checks, and verification procedures implemented across the application.

---

## 1. Test Architecture

The testing strategy validates contracts across all architectural tiers:
- **In-Memory Isolation**: Backend tests run against an isolated in-memory SQLite database (`sqlite+aiosqlite:///:memory:`), ensuring zero test pollution and fast execution.
- **Async Test Execution**: Pytest runs asynchronously via `pytest-asyncio` using HTTPX `AsyncClient` and ASGI transport.
- **TypeScript Static Verification**: The frontend runs strict `tsc` compiler checks verifying prop contracts and API schema alignment.

---

## 2. Test Suites Overview

### A. Curriculum Integrity (`tests/test_curriculum.py`)
- **112 Days Verification**: Tests that exactly 112 lessons exist, day numbers range strictly from 1 through 112 with zero gaps or overlaps, and IDs are unique (`day-001` through `day-112`).
- **Hierarchy Verification**: Validates 4 distinct phases and 16 weeks with milestone relationships.
- **Seeding Idempotency**: Runs `seed_curriculum()` multiple times in succession to verify that repeat execution never duplicates entities or corrupts relationships.
- **Lesson Detail & Navigation**: Tests retrieval by numeric day (e.g. `/api/lessons/1`) and by string ID (`/api/lessons/day-050`), verifying previous/next pointers and structured pedagogical payloads.
- **Search & Filtering**: Tests keyword search (`q=FastAPI`), phase filtering (`phase=3` yielding 28 days), and 404 responses on invalid days.

### B. Progress & State Transitions (`tests/test_progress.py`)
- **Initial Clean State**: Verifies a new learner begins at Day 1 with 0 completed lessons, 0 in-progress lessons, and 0% completion.
- **State Machine Transitions**: Tests transitions between `not_started`, `in_progress`, and `completed`.
- **Validation Discipline**: Tests that bogus or invalid status strings are rejected with HTTP 400 or 422.
- **Accurate Aggregations**: Verifies that progress percentages and counts are calculated directly from source records.

### C. Exercises, Quizzes, Notes & Milestones (`tests/test_quiz_exercise.py`)
- **Quiz Scoring & Feedback**: Submits answer payloads, verifies score calculation (100%), and ensures explanations are returned.
- **Exercise Logging**: Records student execution outputs and notes for hands-on exercises.
- **Study Notes & Bookmarks Persistence**: Tests creating, listing, and deleting study notes and toggling bookmarks.
- **Practice Lab Filtering**: Tests querying practice drills by limit and type.
- **Milestone & Project Updates**: Tests updating milestone task artifacts, Git commit hashes, and verification sign-offs.

---

## 3. Running Automated Tests

### Backend Test Suite
```bash
# Run full Pytest test suite with verbose output
backend/.venv/bin/pytest -v

# Run with test coverage report
backend/.venv/bin/pytest --cov=app tests/
```

### Python Code Quality & Linting
```bash
# Check code style with Ruff
backend/.venv/bin/ruff check app tests

# Check code formatting with Ruff
backend/.venv/bin/ruff format --check app tests
```

### Frontend Type Checking & Production Build
```bash
# Execute TypeScript compiler and Vite asset packaging
npm --prefix frontend run build
```

---

## 4. Test Verification Results

| Test Category | Suite / Command | Execution Status | Verified Output |
| :--- | :--- | :--- | :--- |
| **Curriculum Integrity** | `tests/test_curriculum.py` | **PASSED** | 112 unique days, 16 weeks, 4 phases, idempotent seeding |
| **Progress & Transitions** | `tests/test_progress.py` | **PASSED** | Validated state machine, clean Day 1 start, accurate counts |
| **Quizzes & Exercises** | `tests/test_quiz_exercise.py` | **PASSED** | Quiz evaluation, notes CRUD, bookmark toggling, milestones |
| **Python Linter** | `ruff check app tests` | **PASSED** | 0 lint errors, clean imports |
| **Python Formatter** | `ruff format --check` | **PASSED** | 36 files formatted to PEP 8 standards |
| **TypeScript / Build** | `npm run build` | **PASSED** | 0 TS errors, clean production bundle in `dist/` |
| **SPA Fallback Routing** | Unified ASGI check | **PASSED** | Direct URL `/curriculum/50` returns 200 with index.html |
