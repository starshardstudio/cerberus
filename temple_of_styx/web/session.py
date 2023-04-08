import flask as f

from temple_of_styx.database.tables import Person


def login(person: Person) -> None:
    """
    Log in as the specified person. 
    """
    f.session["LOGIN_PERSON_NAME"] = person.name


def logout() -> None:
    """
    Log out from the current session.
    """
    del f.session["LOGIN_PERSON_NAME"]


__all__ = (
    "login",
    "logout",
)
