import click
import sqlalchemy.sql as sql

from temple_of_styx.database.engine import Session
from temple_of_styx.database.tables import Person


@click.group()
def person():
    pass


@person.command()
@click.argument("name")
def create(name: str) -> None:
    click.echo("Connecting to the database...", err=True)
    with Session() as session:
        click.echo("Creating person...", err=True)
        user = Person(name=name)
        session.add(user)
        session.commit()
        click.echo("Success!", err=True)


@person.command()
@click.argument("name")
@click.argument("password")
def passwd(name: str, password: str) -> None:
    click.echo("Connecting to the database...", err=True)
    with Session() as session:
        click.echo("Finding person...", err=True)
        user = session.execute(sql.select(Person).where(Person.name == name)).scalar_one()
        click.echo("Setting password...", err=True)
        user.set_password(password)
        session.commit()
        click.echo("Success!", err=True)


__all__ = (
    "person",
)