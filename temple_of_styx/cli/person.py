import click

from temple_of_styx.database.engine import Session
from temple_of_styx.database.tables import Person


@click.group()
def person():
    pass


@person.command()
@click.argument("name")
def create(name: str):
    click.echo("Connecting to the database...", err=True)
    with Session() as session:
        click.echo("Creating person...", err=True)
        user = Person(name=name)
        session.add(user)
        session.commit()
        click.echo("Success!", err=True)


__all__ = (
    "person",
)