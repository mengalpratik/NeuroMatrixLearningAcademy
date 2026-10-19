import pytest
from httpx import AsyncClient
from sqlalchemy import func, select

from app.models.curriculum import CurriculumPhase, CurriculumWeek, Lesson
from app.services.seed_data import seed_curriculum


@pytest.mark.asyncio
async def test_curriculum_integrity(client: AsyncClient, test_db):
    async with test_db() as session:
        # Check total phases
        phases_cnt = (
            await session.execute(select(func.count(CurriculumPhase.phase_number)))
        ).scalar()
        assert phases_cnt == 4

        # Check total weeks
        weeks_cnt = (await session.execute(select(func.count(CurriculumWeek.week_number)))).scalar()
        assert weeks_cnt == 16

        # Check total lessons
        lessons_cnt = (await session.execute(select(func.count(Lesson.id)))).scalar()
        assert lessons_cnt == 112

        # Verify contiguous 1..112 day numbers
        days = (
            (await session.execute(select(Lesson.day_number).order_by(Lesson.day_number)))
            .scalars()
            .all()
        )
        assert days == list(range(1, 113))

        # Verify lesson IDs
        ids = (await session.execute(select(Lesson.id))).scalars().all()
        assert len(ids) == 112
        assert len(set(ids)) == 112
        assert "day-001" in ids
        assert "day-112" in ids


@pytest.mark.asyncio
async def test_seeding_idempotency(test_db):
    # Running seed multiple times should not create duplicate lessons or crash
    async with test_db() as session:
        await seed_curriculum(session)
        await seed_curriculum(session)
        lessons_cnt = (await session.execute(select(func.count(Lesson.id)))).scalar()
        assert lessons_cnt == 112


@pytest.mark.asyncio
async def test_api_curriculum_overview(client: AsyncClient):
    response = await client.get("/api/curriculum/overview")
    assert response.status_code == 200
    data = response.json()
    assert data["total_days"] == 112
    assert len(data["phases"]) == 4
    assert data["completed_days"] == 0


@pytest.mark.asyncio
async def test_api_get_lesson_detail(client: AsyncClient):
    # Test by day number
    res1 = await client.get("/api/lessons/1")
    assert res1.status_code == 200
    data1 = res1.json()
    assert data1["id"] == "day-001"
    assert data1["day_number"] == 1
    assert data1["title"] == "Python Setup, Interpreter, Print, Comments & Variables"
    assert len(data1["objectives"]) >= 3
    assert len(data1["concept_sections"]) >= 1
    assert len(data1["code_examples"]) >= 1
    assert len(data1["exercises"]) >= 1
    assert len(data1["quizzes"]) >= 1
    assert data1["prev_day"] is None
    assert data1["next_day"] == 2

    # Test by ID
    res2 = await client.get("/api/lessons/day-050")
    assert res2.status_code == 200
    data2 = res2.json()
    assert data2["day_number"] == 50
    assert "FastAPI" in data2["title"]
    assert data2["prev_day"] == 49
    assert data2["next_day"] == 51

    # Test 404
    res_404 = await client.get("/api/lessons/999")
    assert res_404.status_code == 404


@pytest.mark.asyncio
async def test_api_curriculum_search(client: AsyncClient):
    # Search for FastAPI
    res = await client.get("/api/curriculum/search?q=FastAPI")
    assert res.status_code == 200
    items = res.json()
    assert len(items) >= 1
    assert any(i["day_number"] == 50 for i in items)

    # Filter by phase
    res_phase = await client.get("/api/curriculum/search?phase=3")
    assert res_phase.status_code == 200
    phase_items = res_phase.json()
    assert len(phase_items) == 28  # Days 71 to 98
    assert all(i["phase_number"] == 3 for i in phase_items)
