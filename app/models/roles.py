from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String, TEXT, Table, Column
from app.config.database import Base, TimestampMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.user import User

class Role(Base, TimestampMixin):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    users: Mapped[list["User"]] = relationship(
        back_populates="role",
    )
    permissions: Mapped[list["Permissions"]] = relationship(
        back_populates="roles",
        secondary="role_permissions"
    )

class Permissions(Base, TimestampMixin):
    __tablename__ = "permissions"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(TEXT, nullable=False)
    code_name: Mapped[str] = mapped_column(String(100))
    roles: Mapped[list["Role"]] = relationship(
        back_populates="permissions",
        secondary="role_permissions"
    )

role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column(
        "role_id",
        ForeignKey("roles.id"),
        primary_key=True
    ),
    Column(
        "permission_id",
        ForeignKey("permissions.id"),
        primary_key=True
    )
)

from pydantic import BaseModel, ConfigDict

class RoleResponse(BaseModel):
    id: int
    name: str
    permissions: list[dict] | None = []
    model_config = ConfigDict(
        from_attributes=True
    )

class RoleCreate(BaseModel):
    name: str
    permissions: list[int] | None = []
    model_config = ConfigDict(
        from_attributes=True
    )

class permission(BaseModel):
    name: str
    code_name: str

class PermissionIDsRequest(BaseModel):
    permissions_ids: list[int]
