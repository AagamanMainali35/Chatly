import asyncio
from app.utils.auth import hash_password
from app.config.database import AsyncSession
from app.services.role import RoleService
from app.models.user import User

async def seed_user(user_name:str,email:str,password:str,role_name:str):
    try:
        db=AsyncSession()
        role=await RoleService(db=db).get_role_by_name(name=role_name)
        if not role:
            print(f"{role_name} role not found. Please seed the admin role first.")
            return
        payload={
            "username":user_name,
            "email":email,
            "password":hash_password(password),
            "role_id":role.id
        }        
        instance=User(**payload)
        db.add(instance)
        await db.commit()
        print(f"User {user_name} seeded successfully.")
    except Exception as e:
        print(f"Error seeding users: {e}")
    finally:
        await db.close()
        
        
if __name__=="__main__":
    user_name=input("Enter username: ")
    email=input("Enter email: ")
    password=input("Enter password: ")
    role_name=input("Enter role name: ")
    asyncio.run(seed_user(user_name=user_name,email=email,password=password,role_name=role_name))
