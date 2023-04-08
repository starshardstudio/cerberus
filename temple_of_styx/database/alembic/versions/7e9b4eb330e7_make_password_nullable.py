"""Make password nullable

Revision ID: 7e9b4eb330e7
Revises: c8534aa15b4d
Create Date: 2023-04-08 02:06:20.460947
"""

from alembic import op
import sqlalchemy as sa


revision = "7e9b4eb330e7"
down_revision = "c8534aa15b4d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("people", "password", nullable=True)


def downgrade() -> None:
    op.alter_column("people", "password", nullable=False)
