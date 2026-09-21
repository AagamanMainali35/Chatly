from sqlalchemy import ForeignKey, String, TEXT, Table, Column
from app.config.database import Base, TimestampMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Role(Base, TimestampMixin):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
