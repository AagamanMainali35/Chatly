"""
roles and permission migrations

Revision ID: adae1b800f10
Revises: 00ac42937ac1
Create Date: 2026-10-02 18:10:11.434208
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "adae1b800f10"
down_revision: Union[str, Sequence[str], None] = "00ac42937ac1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "permissions",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    op.add_column(
        "permissions",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    op.add_column(
        "roles",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    op.add_column(
        "roles",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )


def downgrade() -> None:
    op.drop_column("roles", "updated_at")
    op.drop_column("roles", "created_at")
    op.drop_column("permissions", "updated_at")
    op.drop_column("permissions", "created_at")