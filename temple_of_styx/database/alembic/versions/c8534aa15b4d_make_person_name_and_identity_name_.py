"""Make person_name and identity_name foreign keys

Revision ID: c8534aa15b4d
Revises: 5d98543e452c
Create Date: 2023-04-08 02:03:27.211418
"""

from alembic import op
import sqlalchemy as sa


revision = "c8534aa15b4d"
down_revision = "5d98543e452c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key(None, "control", "people", ["person_name"], ["name"])
    op.create_foreign_key(None, "control", "identities", ["identity_name"], ["name"])


def downgrade() -> None:
    op.drop_constraint(None, "control", type_="foreignkey")
    op.drop_constraint(None, "control", type_="foreignkey")
