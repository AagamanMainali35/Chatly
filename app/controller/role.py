from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.models.roles import RoleCreate, RoleResponse
from app.services.role import RoleService

role_router = APIRouter(prefix="/roles")

@role_router.get("/all", response_model=list[RoleResponse])
async def get_roles(db: AsyncSession = Depends(get_db)):
    result = await RoleService(db=db).get_all_roles()
    return result

@role_router.get("/{role_id}", response_model=RoleResponse)
async def get_role_by_id(role_id: int, db: AsyncSession = Depends(get_db)):
    result = await RoleService(db=db).get_role_by_id(role_id=role_id)
    return result
