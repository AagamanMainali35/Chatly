from app.models.roles import Permissions
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_permissions(db: AsyncSession):
    result = await db.execute(select(Permissions))
    permissions = result.scalars().all()
    return permissions

async def get_permission_by_id(id: int, db: AsyncSession):
    result = await db.execute(select(Permissions).where(Permissions.id == id))
    permission = result.scalar_one_or_none()
    return permission

async def get_permissions_by_ids(ids: list[int], db: AsyncSession):
    result = await db.execute(select(Permissions).where(Permissions.id.in_(ids)))
    permissions = result.scalars().all()
    return permissions

async def get_permission_by_name(name: str, db: AsyncSession):
    result = await db.execute(select(Permissions).where(Permissions.name == name))
    permission = result.scalar_one_or_none()
    return permission

async def create_permission(payload: dict, db: AsyncSession):
    permission = Permissions(**payload)
    db.add(permission)
    await db.commit()
    await db.refresh(permission)
    return permission
