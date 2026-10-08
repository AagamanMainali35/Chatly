from app.config.database import AsyncSession
from sqlalchemy import insert 
from app.models.roles  import Permissions as permission
from app.utils.permissionsList import permissions as perm_data
import asyncio
async def seed_perms():
    db=AsyncSession()
    try:
        permissions=[{"name":k,"code_name":v} for k,v in perm_data.items()]
        result=await db.execute(insert(permission).values(permissions).returning(permission))
        await db.commit()
        if result:
            print("Permissions added successfully")
    except Exception as e:
        print(f"Error seeding role: {e}")
    finally :
        await db.close()
           
asyncio.run(seed_perms())
    
    
    
    