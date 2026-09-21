from sqlalchemy import ForeignKey, String, TEXT, Table, Column
from app.config.database import Base, TimestampMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Role(Base, TimestampMixin):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

class Permissions(Base, TimestampMixin):
    __tablename__ = "permissions"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(TEXT, nullable=False)
    code_name: Mapped[str] = mapped_column(String(100))

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
