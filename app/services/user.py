from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.user import create_users, get_user_by_username_or_email
from app.repository.role import fetch_role_by_name
from fastapi import HTTPException
from app.utils.auth import validate_password, hash_password
from sqlalchemy.exc import IntegrityError

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
