from app.repository import permission
from sqlalchemy.ext.asyncio import AsyncSession

class PermissionService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_permissions(self):
        return await permission.get_permissions(db=self.db)

    async def get_permission_by_id(self, id: int):
        existing_permission = await permission.get_permission_by_id(id=id, db=self.db)
        if not existing_permission:
            raise ValueError(f"Permission with id {id} does not exist")
        return existing_permission

    async def get_permissions_by_ids(self, ids: list[int]):
        return await permission.get_permissions_by_ids(ids=ids, db=self.db)

    async def get_permission_by_name(self, name: str):
        perms = await permission.get_permission_by_name(name=name, db=self.db)
        if not perms:
            raise ValueError(f"Permission with name {name} does not exist")
        return perms
