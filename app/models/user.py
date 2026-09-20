from app.config.database import Base, TimestampMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class User(Base, TimestampMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    profile_picture: Mapped[str | None] = mapped_column(nullable=True)

# Model definitions for User entity
from pydantic import BaseModel, EmailStr

class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    profile_picture: str | None = None
