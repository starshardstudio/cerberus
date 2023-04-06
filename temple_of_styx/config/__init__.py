import sqlalchemy as s
import cfig


config = cfig.Configuration()


@config.required()
def DATABASE_URL(value) -> s.URL:
    return s.make_url(value)


@config.required()
def FLASK_SECRET_KEY(value) -> bytes:
    # Generate with `os.urandom`!
    return bytes(value, encoding="utf8")


__all__ = (
    "DATABASE_URL",
    "FLASK_SECRET_KEY",
)
