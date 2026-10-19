from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.schemas.dashboard import DashboardSummaryOut
from app.services.progress_service import get_dashboard_summary

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary", response_model=DashboardSummaryOut)
async def get_summary(user_id: str = settings.DEFAULT_USER_ID, db: AsyncSession = Depends(get_db)):
    return await get_dashboard_summary(db=db, user_id=user_id)
