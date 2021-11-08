"""Docstring."""

import click


@click.command(name="genTransac")
def gen_transac():
    """Docs."""
    click.echo("genTransac")


@click.command(name="genIdenti")
def gen_identi():
    """Docs."""
    click.echo("genIdenti")


class Identity:
    """Docs."""

    def __init__(self,name,password):
        self.name=name
        self.password=password
