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
