from app.services.role import RoleService
from app.services.permission import PermissionService
from app.config.database import AsyncSession
import asyncio

async def seed_role():
    db = AsyncSession()
    try:
        result = await PermissionService(db=db).get_permissions()
        print("Permissions:", result)
    finally:
        await db.close()

if __name__ == "__main__":
    asyncio.run(seed_role())
