import flask


def json(func):
    """
    Call :func:`flask.jsonify` on the returned value.
    """
    return lambda *args, **kwargs: flask.jsonify(func(*args, **kwargs))


__all__ = (
    "json",
)
