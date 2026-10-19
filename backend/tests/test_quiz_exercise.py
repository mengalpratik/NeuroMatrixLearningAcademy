import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_quiz_submission_and_scoring(client: AsyncClient):
    # Fetch Day 1 to get question IDs
    lesson_res = await client.get("/api/lessons/1")
    lesson = lesson_res.json()
    quizzes = lesson["quizzes"]
    assert len(quizzes) >= 1

    q1 = quizzes[0]
    # Submit correct answer
    submission = {
        "answers": [
            {
                "question_id": q1["id"],
                "selected_answer": "Compiles source into bytecode, which runs on the Python Virtual Machine (PVM)",
            }
        ]
    }
    submit_res = await client.post("/api/lessons/1/quiz/submit", json=submission)
    assert submit_res.status_code == 200
    res_data = submit_res.json()
    assert res_data["total_questions"] == 1
    assert res_data["correct_count"] == 1
    assert res_data["score_percentage"] == 100.0
    assert res_data["results"][0]["is_correct"] is True


@pytest.mark.asyncio
async def test_exercise_attempt_submission(client: AsyncClient):
    lesson_res = await client.get("/api/lessons/1")
    lesson = lesson_res.json()
    ex1 = lesson["exercises"][0]

    attempt_payload = {
        "submitted_output": "=== NEUROMATRIX NODE STATUS ===\nDevice: AlphaSentinel [192.168.1.105]\nStatus: ACTIVE | Latency: 14.2ms\n===============================",
        "notes": "Verified locally in terminal with python3 status.py",
    }
    res = await client.post(f"/api/lessons/1/exercises/{ex1['id']}/submit", json=attempt_payload)
    assert res.status_code == 200
    data = res.json()
    assert data["exercise_id"] == ex1["id"]
    assert data["status"] == "passed"
    assert "Verified locally" in data["notes"]


@pytest.mark.asyncio
async def test_notes_and_bookmarks_persistence(client: AsyncClient):
    # Save note
    note_payload = {
        "lesson_id": "day-001",
        "day_number": 1,
        "title": "Day 1 CPython Notes",
        "content": "Bytecode is stored in __pycache__ and executed on the PVM.",
    }
    note_res = await client.post("/api/notes", json=note_payload)
    assert note_res.status_code == 200
    note_data = note_res.json()
    assert note_data["title"] == "Day 1 CPython Notes"

    # List notes
    notes_list = (await client.get("/api/notes")).json()
    assert len(notes_list) >= 1
    assert any(n["title"] == "Day 1 CPython Notes" for n in notes_list)

    # Toggle bookmark
    bm_res = await client.post(
        "/api/bookmarks/toggle", json={"lesson_id": "day-001", "day_number": 1}
    )
    assert bm_res.status_code == 200
    assert bm_res.json()["is_bookmarked"] is True

    # Check lesson detail reflects bookmark and note
    lesson_after = (await client.get("/api/lessons/1")).json()
    assert lesson_after["is_bookmarked"] is True
    assert "Bytecode is stored in __pycache__" in lesson_after["current_note"]

    # Toggle bookmark off
    bm_off = await client.post(
        "/api/bookmarks/toggle", json={"lesson_id": "day-001", "day_number": 1}
    )
    assert bm_off.status_code == 200
    assert bm_off.json()["is_bookmarked"] is False


@pytest.mark.asyncio
async def test_practice_lab_and_milestones(client: AsyncClient):
    # Practice questions
    practice_res = await client.get("/api/practice/questions?limit=5")
    assert practice_res.status_code == 200
    questions = practice_res.json()
    assert len(questions) == 5

    # Milestone verification
    m_payload = {
        "evidence_notes": "Completed CLI implementation, verified with exit code 0",
        "status": "verified",
    }
    m_res = await client.post("/api/milestones/1/verify", json=m_payload)
    assert m_res.status_code == 200
    assert m_res.json()["status"] == "verified"

    # Project task update
    task_update = {
        "status": "completed",
        "git_commit_ref": "git commit 78a9bc0",
        "implementation_notes": "Implemented device status lookup with ANSI formatting",
    }
    p_res = await client.patch("/api/projects/task-w01-milestone", json=task_update)
    assert p_res.status_code == 200
    assert p_res.json()["status"] == "completed"
    assert p_res.json()["git_commit_ref"] == "git commit 78a9bc0"
