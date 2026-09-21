from typing import TYPE_CHECKING
from pydantic import BaseModel, ConfigDict , EmailStr
from sqlalchemy import DateTime,Index,ForeignKey,String , TEXT , Table , Column
from app.config.database import Base , TimestampMixin
from sqlalchemy.orm import Mapped , mapped_column ,relationship 

if TYPE_CHECKING:
    from app.models.roles import Role

class User(Base, TimestampMixin):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    role_id:Mapped[int]=mapped_column(ForeignKey("roles.id"),nullable=False)
    username:Mapped[str]=mapped_column(unique=True, nullable=False)
    email:Mapped[str]=mapped_column(nullable=False)
    password:Mapped[str]=mapped_column(nullable=False)
    profile_picture:Mapped[str|None]=mapped_column(nullable=True)
    role:Mapped["Role"]=relationship(
        back_populates="users",
    )
    
# Schema for the user model
class UserCreateSchema(BaseModel):
    username:str
    email:EmailStr
    password:str
    profile_picture:str|None=None
    


