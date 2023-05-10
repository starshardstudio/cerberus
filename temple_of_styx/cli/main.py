import click

from .person import person
from .identity import identity


@click.group()
def main():
    pass


main.add_command(person)
main.add_command(identity)
