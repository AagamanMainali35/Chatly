from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.models.roles import permission, permissionResponse, PermissionIDsRequest, PermissionUpdate
from app.services.permission import PermissionService

permission_router = APIRouter(prefix="/permissions")

@permission_router.get("/all", response_model=list[permissionResponse])
async def get_permissions(db: AsyncSession = Depends(get_db)):
    result = await PermissionService(db=db).get_permissions()
    return result

@permission_router.post("/ids", response_model=list[permissionResponse])
async def get_permissions_by_ids(ids: PermissionIDsRequest, db: AsyncSession = Depends(get_db)):
    result = await PermissionService(db=db).get_permissions_by_ids(ids=ids.permissions_ids)
    return result
