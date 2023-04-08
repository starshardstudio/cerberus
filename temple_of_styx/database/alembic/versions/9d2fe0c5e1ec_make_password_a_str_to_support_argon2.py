"""Make password a str to support argon2

Revision ID: 9d2fe0c5e1ec
Revises: 7e9b4eb330e7
Create Date: 2023-04-08 16:34:41.691687
"""

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects import postgresql


revision = "9d2fe0c5e1ec"
down_revision = "7e9b4eb330e7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        "people",
        "password",
        existing_type=sa.LargeBinary,
        type_=sa.String,
        nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "people",
        "password",
        existing_type=sa.String,
        type_=sa.LargeBinary,
        nullable=True,
    )
