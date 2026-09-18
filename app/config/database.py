
from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.config.settings import settings

engine=create_async_engine(str(settings.DATABASE_URL)) # because the pydantic settings converts to dns but engine expects the string URL
AsyncSession=async_sessionmaker(bind=engine,expire_on_commit=False)  

async def get_db():
    async with AsyncSession() as session:
        try:
            yield session 
        except Exception:
            await session.rollback()
            raise

# Declarative Base for models
class Base(DeclarativeBase):
    pass

#Timestamp mixin 
class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )