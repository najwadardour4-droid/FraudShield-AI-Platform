from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    DATABASE_URL: str = f"sqlite+aiosqlite:///{(BACKEND_ROOT / 'fraud_platform.db').as_posix()}"
    SECRET_KEY: str = "pfe-fraud-detection-dev-secret-key-change-in-prod"
    API_PREFIX: str = "/api/v1"
    MODEL_DIR: str = "ml_models"
    CORS_ORIGINS: str = "http://localhost:4200"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480
    FRAUD_THRESHOLD: float = 0.5

    @property
    def model_path(self) -> Path:
        return BACKEND_ROOT / self.MODEL_DIR

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]


settings = Settings()
