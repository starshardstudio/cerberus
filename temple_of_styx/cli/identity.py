import click
import sqlalchemy.sql as sql

from temple_of_styx.database.engine import Session
from temple_of_styx.database.tables import Person, Identity, Control


@click.group()
def identity():
    pass


@identity.command()
@click.argument("owner")
@click.argument("identity")
def create(owner: str, identity: str):
    click.echo("Connecting to the database...", err=True)
    with Session() as session:
        click.echo("Finding person...", err=True)
        user = session.execute(sql.select(Person).where(Person.name == owner)).scalar_one()
        click.echo("Creating identity and giving full control to the owner...", err=True)
        identity = Identity(name=identity)
        session.add(identity)
        control = Control(person=user, identity=identity)
        session.add(control)
        session.commit()
        click.echo("Success!", err=True)
