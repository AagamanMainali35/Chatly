# config.py
from typing import List

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    secret_key: str
    jwt_algorithm: str
    cors_allowed_origins:str

    model_config = SettingsConfigDict(env_file=".env",case_sensitive=False)
    
    @property
    def cors_origins(self)->List[str]:
        return [origin.strip() for origin in self.cors_allowed_origins.split(",") if origin.strip()]

settings = Settings()