import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.curriculum import router as curriculum_router
from app.api.dashboard import router as dashboard_router
from app.api.exercises import router as exercises_router
from app.api.health import router as health_router
from app.api.notes import router as notes_router
from app.api.practice import router as practice_router
from app.api.progress import router as progress_router
from app.api.projects import router as projects_router
from app.api.quiz import router as quiz_router
from app.core.config import settings
from app.core.database import async_session_factory, init_db
from app.services.seed_data import seed_curriculum

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("neuromatrix.academy")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing NeuroMatrix Academy database...")
    await init_db()
    async with async_session_factory() as session:
        logger.info("Seeding 112-day curriculum & initial milestones...")
        await seed_curriculum(session)
    logger.info("NeuroMatrix Academy startup complete. Ready for learning.")
    yield
    logger.info("NeuroMatrix Academy shutting down.")


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Full-Stack Learning & Engineering Platform for 112-Day Python Mastery",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers
api_prefix = settings.API_V1_STR
app.include_router(health_router, prefix=api_prefix)
app.include_router(dashboard_router, prefix=api_prefix)
app.include_router(curriculum_router, prefix=api_prefix)
app.include_router(progress_router, prefix=api_prefix)
app.include_router(exercises_router, prefix=api_prefix)
app.include_router(quiz_router, prefix=api_prefix)
app.include_router(practice_router, prefix=api_prefix)
app.include_router(projects_router, prefix=api_prefix)
app.include_router(notes_router, prefix=api_prefix)

from fastapi.responses import FileResponse, JSONResponse

# Mount frontend production build and handle SPA routing
frontend_dist = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"
index_html = frontend_dist / "index.html"
assets_dir = frontend_dist / "assets"

if assets_dir.exists():
    app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="frontend_assets")


@app.get("/{full_path:path}", include_in_schema=False)
async def serve_spa(full_path: str):
    if full_path.startswith("api"):
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="API endpoint not found")

    candidate = frontend_dist / full_path
    if candidate.is_file():
        return FileResponse(candidate)

    if index_html.exists():
        return FileResponse(index_html)

    return JSONResponse(
        {"message": "NeuroMatrix Academy API is running. Build frontend to view UI."},
        status_code=200,
    )
