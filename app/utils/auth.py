from pwdlib import PasswordHash
from jwt import encode, decode, ExpiredSignatureError, InvalidTokenError
from pydantic import ValidationError
from app.config.database import get_db
from app.config.settings import settings
from fastapi import Depends, HTTPException , Request
from datetime import datetime, timedelta, timezone
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User, UserCreateSchema
import re

scheme = HTTPBearer()

_hasher = PasswordHash.recommended()

def hash_password(password: str):
    return _hasher.hash(password)


def decode_password(new_password: str, old_password: str):
    return _hasher.verify(new_password, old_password)


def create_access_token(user_id):
    payload = {
        "sub": user_id,
        "type": "access",
        "expiry": datetime.now(timezone.utc) + timedelta(minutes=30),
    }
    return encode(payload)


def create_refresh_token(user_id):
    payload = {
        "sub": user_id,
        "type": "refresh",
        "expiry": datetime.now(timezone.utc) + timedelta(days=7),
    }
    return encode(payload)


def decode_token(token):
    try:
        decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired.",
        )

    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token provided.",
        )


def validate_password(password: str):
    if len(password) < 8:
        return False, "Password must be at least 8 characters"

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"

    if not re.search(r"\d", password):
        return False, "Password must contain at least one number"

    if not re.search(r"[^A-Za-z\d]", password):
        return False, "Password must contain at least one special character"

    return True, "Password is valid"
    
    
from fastapi import Form

def get_user_payload(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
):
    try:
        return UserCreateSchema(
            username=username,
            email=email,
            password=password,
        )
    except ValidationError as e:
            raise HTTPException(status_code=400 , detail=e.errors())
        
    
async def get_current_user(
    request: Request,
    db: AsyncSession = Depends(get_db),
    _=Depends(scheme),
):
    user_obj = await db.execute(
        select(User).where(User.id == request.state.user_id)
    )

    return user_obj.scalar_one_or_none()