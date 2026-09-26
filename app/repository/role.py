from sqlalchemy.ext.asyncio import AsyncSession
from app.models.roles import Role
from sqlalchemy import select, orm
from app.repository.permission import get_permissions_by_ids

async def fetch_roles(db: AsyncSession):
    result = await db.execute(select(Role).options(orm.selectinload(Role.permissions)))
    roles = result.scalars().all()
    return roles
