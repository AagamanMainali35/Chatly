from sqlalchemy import select
from app.models.roles import Role
from app.repository.role import insert_role, delete_role as delete_role_repo, fetch_role_by_id, fetch_roles, update_role
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

class RoleService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_role(self, role: dict):
        existing_role = await self.db.execute(select(Role).where(Role.name == role["name"].lower()))
        if existing_role.scalar_one_or_none():
            raise HTTPException(detail="Role with this name already exists", status_code=409)
        permissions = role.pop("permissions", None)
        if permissions is not None:
            role["permissions"] = permissions
        result = await insert_role(payload=role, db=self.db)
        return result

    async def get_all_roles(self):
        result = await fetch_roles(db=self.db)
        return result

    async def get_role_by_id(self, role_id: int):
        existing_role = await fetch_role_by_id(id=role_id, db=self.db)
        if not existing_role:
            raise HTTPException(detail="Role with this id does not exist", status_code=404)
        return existing_role
