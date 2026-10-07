from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import UploadFile , File ,Form
from app.config.database import get_db
from app.models.user import UserCreateSchema
from app.services.user import UserService
from app.utils.auth import get_user_payload

router = APIRouter()


@router.post("/register")
async def register(
    payload: UserCreateSchema=Depends(get_user_payload),
    db: AsyncSession = Depends(get_db),
    profile_picture:UploadFile=File()
):
    payload=UserCreateSchema.model_validate(payload)
    return await UserService(db=db).register_user(
        payload=payload.model_dump(exclude_unset=True),file=profile_picture)

@router.post("/login")
async def register(db:AsyncSession=Depends(get_db)):
    ...

@router.post("/change-password")
async def register(db:AsyncSession=Depends(get_db)):
    ...
    
@router.post("/reset-password")
async def register(db:AsyncSession=Depends(get_db)):
    ...