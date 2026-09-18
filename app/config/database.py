from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config.settings import settings

engine = create_async_engine(str(settings.DATABASE_URL))
AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False)
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
