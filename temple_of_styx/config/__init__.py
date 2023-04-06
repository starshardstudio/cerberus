import sqlalchemy as s
import cfig


config = cfig.Configuration()


@config.required(key="DATABASE_URL")
def DATABASE_URL(value) -> s.URL:
    return s.make_url(value)


__all__ = (
    "DATABASE_URL",
)
