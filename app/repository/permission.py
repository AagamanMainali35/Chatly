from app.models.roles import Permissions
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_permissions(db: AsyncSession):
    result = await db.execute(select(Permissions))
    permissions = result.scalars().all()
    return permissions
