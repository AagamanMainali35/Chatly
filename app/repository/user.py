from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import or_, select, insert, update, delete
from app.models.user import User

async def get_users(db: AsyncSession):
    query = select(User)
    result = await db.execute(query)
    return result.scalars().all()

async def get_user_by_username_or_email(
    username: str | None,
    email: str | None,
    db: AsyncSession
):
    "search the db for a user with matching email or username"
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

async def create_users(payload: dict, db: AsyncSession):
    "Query function to insert a new user in the database"
    query = insert(User).values(**payload).returning(User)
    result = await db.execute(query)
    await db.commit()
    return result.scalar_one()
