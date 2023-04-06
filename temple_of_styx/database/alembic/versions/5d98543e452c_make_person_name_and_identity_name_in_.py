"""Make person_name and identity_name in the control table non-nullable

Revision ID: 5d98543e452c
Revises: 28836f4b5c49
Create Date: 2023-04-06 23:35:03.490347
"""

from alembic import op
import sqlalchemy as sa


revision = "5d98543e452c"
down_revision = "28836f4b5c49"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("control", "person_name", nullable=False)
    op.alter_column("control", "identity_name", nullable=False)


def downgrade() -> None:
    op.alter_column("control", "person_name", nullable=True)
    op.alter_column("control", "identity_name", nullable=True)
