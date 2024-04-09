import cfig
import sqlalchemy as s

config = cfig.Configuration()


@config.required()
def DATABASE_URL(value) -> s.URL:
    return s.make_url(value)


@config.required()
def WERKZEUG_PROXY_FOR_COUNT(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise cfig.InvalidValueError("Not a valid int.")


@config.required()
def WERKZEUG_PROXY_PROTO_COUNT(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise cfig.InvalidValueError("Not a valid int.")


@config.required()
def WERKZEUG_PROXY_HOST_COUNT(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise cfig.InvalidValueError("Not a valid int.")


@config.required()
def WERKZEUG_PROXY_PREFIX_COUNT(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise cfig.InvalidValueError("Not a valid int.")


@config.required()
def FLASK_SECRET_KEY(value) -> bytes:
    # Generate with `os.urandom`!
    return bytes(value, encoding="utf8")


@config.required()
def STYX_TITLE(value) -> str:
    return value


@config.required()
def STYX_ID(value) -> str:
    return value


@config.required()
def STYX_BLUELIB_COLORS(value) -> str:
    """
    The name of the colors stylesheet to load, without the prefix.
    For example, `royalblue`.
    """
    return value


__all__ = (
    "DATABASE_URL",
    "WERKZEUG_PROXY_FOR_COUNT",
    "WERKZEUG_PROXY_PROTO_COUNT",
    "WERKZEUG_PROXY_HOST_COUNT",
    "WERKZEUG_PROXY_PREFIX_COUNT",
    "FLASK_SECRET_KEY",
    "STYX_TITLE",
    "STYX_BLUELIB_COLORS",
)
