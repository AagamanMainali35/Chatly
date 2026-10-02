"""Added composite primary key

Revision ID: 1cb0ba7d3777
Revises: adae1b800f10
Create Date: 2026-10-02 21:08:06.088960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cb0ba7d3777'
down_revision: Union[str, Sequence[str], None] = 'adae1b800f10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "role_permissions_pkey",
        "role_permissions",
        type_="primary"
    )

    op.alter_column(
        "role_permissions",
        "permission_id",
        existing_type=sa.INTEGER(),
        nullable=False
    )

    op.create_primary_key(
        "role_permissions_pkey",
        "role_permissions",
        ["role_id", "permission_id"]
    )


def downgrade() -> None:
    op.drop_constraint(
        "role_permissions_pkey",
        "role_permissions",
        type_="primary"
    )

    op.alter_column(
        "role_permissions",
        "permission_id",
        existing_type=sa.INTEGER(),
        nullable=True
    )

    op.create_primary_key(
        "role_permissions_pkey",
        "role_permissions",
        ["role_id"]
    )
    # ### end Alembic commands ###