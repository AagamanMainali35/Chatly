from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.user import create_users, get_user_by_username_or_email
from app.repository.role import fetch_role_by_name
from fastapi import HTTPException
from app.utils.auth import validate_password, hash_password
from sqlalchemy.exc import IntegrityError

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    def validate_password(self, password):
        result, message = validate_password(password)
        if not result:
            raise HTTPException(status_code=400, detail=message)
        hashed_password = hash_password(password)
        return hashed_password

    async def register_user(self, payload: dict):
        search_user = await get_user_by_username_or_email(
            username=payload["username"], email=payload["email"], db=self.db
        )
        if search_user is not None:
            raise HTTPException(
                status_code=409,
                detail="User already exists",
            )
