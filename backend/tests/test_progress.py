import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_dashboard_initial_state(client: AsyncClient):
    res = await client.get("/api/dashboard/summary")
    assert res.status_code == 200
    data = res.json()
    assert data["total_days"] == 112
    assert data["completed_days"] == 0
    assert data["in_progress_days"] == 0
    assert data["remaining_days"] == 112
    assert data["completion_percentage"] == 0.0
    assert data["current_day"] == 1
    assert data["today_lesson"]["day_number"] == 1
    assert data["today_lesson"]["status"] == "not_started"


@pytest.mark.asyncio
async def test_lesson_status_transition(client: AsyncClient):
    # Transition Day 1 to in_progress
    res1 = await client.post("/api/lessons/1/status", json={"status": "in_progress"})
    assert res1.status_code == 200
    prog1 = res1.json()
    assert prog1["status"] == "in_progress"
    assert prog1["started_at"] is not None
    assert prog1["completed_at"] is None

    # Check dashboard reflects in_progress
    dash1 = (await client.get("/api/dashboard/summary")).json()
    assert dash1["in_progress_days"] == 1
    assert dash1["completed_days"] == 0
    assert dash1["current_day"] == 1

    # Transition Day 1 to completed
    res2 = await client.post("/api/lessons/1/status", json={"status": "completed"})
    assert res2.status_code == 200
    prog2 = res2.json()
    assert prog2["status"] == "completed"
    assert prog2["completed_at"] is not None

    # Check dashboard updates to Day 2 as active, 1 completed
    dash2 = (await client.get("/api/dashboard/summary")).json()
    assert dash2["completed_days"] == 1
    assert dash2["in_progress_days"] == 0
    assert dash2["current_day"] == 2
    assert dash2["completion_percentage"] > 0.0
    assert len(dash2["recent_activities"]) >= 2


@pytest.mark.asyncio
async def test_invalid_status_transition(client: AsyncClient):
    res = await client.post("/api/lessons/1/status", json={"status": "invalid_bogus_status"})
    assert res.status_code in (400, 422)
