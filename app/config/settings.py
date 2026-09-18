from typing import List
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)
