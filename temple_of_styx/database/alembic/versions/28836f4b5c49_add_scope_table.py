"""Add scope table

Revision ID: 28836f4b5c49
Revises: 8e3138907201
Create Date: 2023-04-06 23:32:52.903140
"""

from alembic import op
import sqlalchemy as sa


revision = "28836f4b5c49"
down_revision = "8e3138907201"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "scopes",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("control_id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["control_id"],
            ["control.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("scopes")
