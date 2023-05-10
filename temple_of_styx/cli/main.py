import click

from .person import person


@click.group()
def main():
    pass


main.add_command(person)
