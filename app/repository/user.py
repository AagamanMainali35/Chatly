from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.config.database import get_db
from sqlalchemy import or_, select , insert , update , delete  
from app.models.user import User

async def get_users(db:AsyncSession):
    query=select(User)
    result=await db.execute(query)
    return result.scalars().all()

async def create_users(payload:dict,db:AsyncSession):
    "Query function to insert a new user in the database"
    query=insert(User).values(**payload).returning(User)
    result=await db.execute(query)
    await db.commit()
    return result.scalar_one()
    
async def get_user_by_id(id:int,db:AsyncSession):
    query=select(User).where(User.id==id)
    result=await db.execute(query)
    return result.scalar_one_or_none()
    
async def get_user_by_username_or_email(
    username: str | None ,
    email: str | None ,
    db:AsyncSession
):
    "search the db for a user with matching email or password "
    if not username and not email:
        return None

    conditions = []

    if username:
        conditions.append(User.username == username)

    if email:
        conditions.append(User.email == email)

    query = select(User).where(or_(*conditions))

    result = await db.execute(query)

    return result.scalar_one_or_none()
    
async def remove_users(db:AsyncSession):
    query= delete(User)
    result=await db.execute(query)
    await db.commit()
    return {"deleted": result.rowcount}
    
async def remove_user(id:int,db:AsyncSession):
    query= delete(User).where(User.id==id)
    result=await db.execute(query)
    await db.commit()
    return result.rowcount
    
    
async def update_users(payload:dict,db:AsyncSession):
    ...
