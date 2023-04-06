import flask_sqlalchemy

from temple_of_styx.database.tables import Base


ext_sqla: flask_sqlalchemy.SQLAlchemy = flask_sqlalchemy.SQLAlchemy(
    metadata=Base.metadata,
    add_models_to_shell=True,
)


__all__ = (
    "ext_sqla",
)
