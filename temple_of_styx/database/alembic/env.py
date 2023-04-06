from sqlalchemy import create_engine
from alembic import context

from ...config import DATABASE_URL
from ..tables import Base


def run_migrations_offline() -> None:
    context.configure(
        url=DATABASE_URL.__wrapped__,
        target_metadata=Base.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    engine = create_engine(DATABASE_URL.__wrapped__)

    with engine.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=Base.metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
