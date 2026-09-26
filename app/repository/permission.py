from app.models.roles import Permissions
from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession

async def get_permissions(db:AsyncSession):
    result=await db.execute(select(Permissions))
    permissions=result.scalars().all()
    return permissions

async def get_permission_by_id(id:int,db:AsyncSession):
    result=await db.execute(select(Permissions).where(Permissions.id==id))
    permission=result.scalar_one_or_none()
    return permission

async def get_permissions_by_ids(ids:list[int],db:AsyncSession):
    result=await db.execute(select(Permissions).where(Permissions.id.in_(ids)))
    permissions=result.scalars().all()
    return permissions

async def get_permission_by_name(name:str,db:AsyncSession):
    result=await db.execute(select(Permissions).where(Permissions.name==name))
    permission=result.scalar_one_or_none()
    return permission

async def create_permission(payload:dict,db:AsyncSession):
    permission=Permissions(**payload)
    db.add(permission)
    await db.commit()
    await db.refresh(permission)
    return permission

async def update_permission(id:int,payload:dict,db:AsyncSession):
    permission=await get_permission_by_id(id=id,db=db)
    if not permission:
        return None
    for key,value in payload.items():
        setattr(permission,key,value)
    db.add(permission)
    await db.commit()
    await db.refresh(permission)
    return permission

async def delete_permission(id:int,db:AsyncSession):
    permission=await get_permission_by_id(id=id,db=db)
    if not permission:
        return None
    await db.delete(permission)
    await db.commit()
    return permission