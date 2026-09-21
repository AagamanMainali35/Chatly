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
