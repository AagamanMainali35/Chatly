# config.py
from typing import List

from pydantic import PostgresDsn, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    secret_key: str
    jwt_algorithm: str
    cors_allowed_origins: str

    s3_endpoint: HttpUrl
    s3_public_endpoint: HttpUrl | None = None   # keep the field, no property of the same name
    s3_access_key: str
    s3_secret_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def cors_origins(self) -> List[str]:
        return [o.strip() for o in self.cors_allowed_origins.split(",") if o.strip()]

    @property
    def _s3_endpoint(self) -> str:
        # fall back to internal endpoint when not set
        return str(self.s3_public_endpoint or self.s3_endpoint)


settings = Settings()