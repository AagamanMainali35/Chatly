from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import get_db
from app.models.roles import permission,permissionResponse , PermissionIDsRequest , PermissionUpdate
from app.services.permission import PermissionService
permission_router=APIRouter(prefix="/permissions")

@permission_router.get("/all",response_model=list[permissionResponse])
async def get_permissions(db:AsyncSession=Depends(get_db)):
    result=await PermissionService(db=db).get_permissions()
    return result   
    
@permission_router.post("/ids",response_model=list[permissionResponse])
async def get_permissions_by_ids(ids:PermissionIDsRequest,db:AsyncSession=Depends(get_db)):
    result=await PermissionService(db=db).get_permissions_by_ids(ids=ids.permissions_ids)
    return result

@permission_router.get("/name/{name}",response_model=permissionResponse)
async def get_permission_by_name(name:str,db:AsyncSession=Depends(get_db)):
    try:
        result=await PermissionService(db=db).get_permission_by_name(name=name)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))
    
@permission_router.post("/create",response_model=permissionResponse)
async def create_permission(permission:permission,db:AsyncSession=Depends(get_db)):
    payload={"name":permission.name,"code_name":permission.code_name}
    result=await PermissionService(db=db).create_permission(payload=payload)
    return result

@permission_router.get("/{id}",response_model=permissionResponse)
async def get_permission_by_id(id:int,db:AsyncSession=Depends(get_db)):
    try:
        result=await PermissionService(db=db).get_permission_by_id(id=id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@permission_router.patch("/update/{id}",response_model=permissionResponse)
async def update_permission(id:int,permission:PermissionUpdate,db:AsyncSession=Depends(get_db
)):
    payload=permission.model_dump(exclude_unset=True)
    try:
        result=await PermissionService(db=db).update_permission(id=id,payload=payload)
        if not result:
            raise HTTPException(status_code=404,detail=f"Permission with id {id} does not exist")
        return result
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))
    
    
@permission_router.delete("/delete/{id}")
async def delete_permission(id:int,db:AsyncSession=Depends(get_db)):
    try:
        _=await PermissionService(db=db).delete_permission(id=id)
        return {"message":"Permission deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))
