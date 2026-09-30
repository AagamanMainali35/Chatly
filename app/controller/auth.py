from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db
from app.models.user import UserCreateSchema
from app.services.user import UserService

router = APIRouter()


@router.post("/register")
async def register(
    payload: UserCreateSchema,
    db: AsyncSession = Depends(get_db),
):
    print(payload)
    return await UserService(db=db).register_user(
        payload=payload.model_dump(exclude_unset=True))

@router.post("/login")
async def register(db:AsyncSession=Depends(get_db)):
    ...

@router.post("/change-password")
async def register(db:AsyncSession=Depends(get_db)):
    ...
    
@router.post("/reset-password")
async def register(db:AsyncSession=Depends(get_db)):
    ...