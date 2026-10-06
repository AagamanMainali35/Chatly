# config.py
from typing import List

from pydantic import PostgresDsn , HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


# # Storage configuration 
# S3_ENDPOINT=http://minio:9000
# S3_ACCESS_KEY=your_minio_username
# S3_SECRET_KEY=your_minio_password
# S3_BUCKET=chat-files
# S3_REGION=us-east-1
# S3_SECURE=false

class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    secret_key: str
    jwt_algorithm: str
    cors_allowed_origins:str
    s3_endpoint:HttpUrl
    s3_public_endpoint:HttpUrl | None = None
    s3_access_key:str
    s3_secret_key:str
    
    

    model_config = SettingsConfigDict(env_file=".env",case_sensitive=False,extra="ignore")
    
    @property
    def cors_origins(self)->List[str]:
        return [origin.strip() for origin in self.cors_allowed_origins.split(",") if origin.strip()]

settings = Settings()