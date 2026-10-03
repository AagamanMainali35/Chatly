from app.services.role import RoleService
from app.services.permission import PermissionService
from app.config.database import AsyncSession
import asyncio
from rich.pretty import pprint
import re

async def seed_role():
    try:
        db=AsyncSession()
        result=await PermissionService(db=db).get_permissions()
        data=[{"id":perm.id,"name":perm.name} for perm in result]
        print("The available permissions are :")
        pprint(data)
        name=input("Enter the role_name: ")
        perms_ids=input("Enter the permission ids eg: (1) or (1,2,3): ")
        if not re.match(r"^\d+(?:,\d+)*$",perms_ids):
            pprint("Invalid id provided eg: (1) or (1,2,3)")
            return
        perms_ids=[int(perm_id) for perm_id in perms_ids.split(",")]
        payload={
            "name":name,
            "is_system":True,
            "permissions":perms_ids
        }
        result= await RoleService(db=db).create_role(role=payload)
        if result:
            pprint({"status":True,"message":"Role creation successful"})
    except Exception as e:
        print(f"Error seeding role: {e}")
    finally:
        await db.close()      
asyncio.run(seed_role())