from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.models.user import UserCreateSchema
from app.services.user import UserService

router = APIRouter()
