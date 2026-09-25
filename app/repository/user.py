from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import or_, select, insert, update, delete
from app.models.user import User

async def get_users(db: AsyncSession):
    query = select(User)
    result = await db.execute(query)
    return result.scalars().all()
