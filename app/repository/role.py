from sqlalchemy.ext.asyncio import AsyncSession
from app.models.roles import Role
from sqlalchemy import select, orm
from app.repository.permission import get_permissions_by_ids

async def fetch_roles(db: AsyncSession):
    result = await db.execute(select(Role).options(orm.selectinload(Role.permissions)))
    roles = result.scalars().all()
    return roles

async def fetch_role_by_name(name: str, db: AsyncSession):
    result = await db.execute(select(Role).where(Role.name == name))
    role = result.scalar_one_or_none()
    return role

async def fetch_role_by_id(id: int, db: AsyncSession):
    result = await db.execute(select(Role).options(orm.selectinload(Role.permissions)).where(Role.id == id))
    role = result.scalar_one_or_none()
    return role

async def insert_role(payload: dict, db: AsyncSession):
    permissions = payload.pop("permissions", [])
    role = Role(**payload)
    if permissions:
        role.permissions = await get_permissions_by_ids(ids=permissions, db=db)
    db.add(role)
    await db.commit()
    await db.refresh(role)
    return role
