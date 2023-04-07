import flask_sqlalchemy
from authlib.integrations.flask_oauth2 import AuthorizationServer
from authlib.integrations.sqla_oauth2 import create_query_client_func, create_save_token_func

from temple_of_styx.database.tables import Base, Client, Token


ext_sqla: flask_sqlalchemy.SQLAlchemy = flask_sqlalchemy.SQLAlchemy(
    metadata=Base.metadata,
    add_models_to_shell=True,
)

ext_auth: AuthorizationServer = AuthorizationServer(
    query_client=create_query_client_func(
        session=ext_sqla.session,
        client_model=Client,
    ),
    save_token=create_save_token_func(
        session=ext_sqla.session,
        token_model=Token,
    )
)


__all__ = (
    "ext_sqla",
    "ext_auth",
)
