from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    PROJECT_NAME: str = "NeuroMatrix Learning Academy"
    API_V1_STR: str = "/api"
    DATABASE_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/neuromatrix_academy.db"
    SYNC_DATABASE_URL: str = f"sqlite:///{BASE_DIR}/neuromatrix_academy.db"
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]
    DEFAULT_USER_ID: str = "learner-prime"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="ignore"
    )


settings = Settings()
