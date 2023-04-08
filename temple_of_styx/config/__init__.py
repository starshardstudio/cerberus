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


@config.required()
def STYX_TITLE(value) -> str:
    return value


@config.required()
def STYX_BLUELIB_COLORS(value) -> str:
    """
    The name of the colors stylesheet to load, without the prefix.
    For example, `royalblue`.
    """
    return value


@config.required()
def STYX_BACKGROUND_SRC(value) -> str:
    """
    The background image to display on the page.
    For example, `https://bluelib.steffo.eu/examples/fabrice-nerfin-puHQJZd3MDg-unsplash.jpg`.
    """
    return value


__all__ = (
    "DATABASE_URL",
    "FLASK_SECRET_KEY",
    "STYX_TITLE",
    "STYX_BLUELIB_COLORS",
    "STYX_BACKGROUND_SRC",
)
