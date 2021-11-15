"""Docstring."""

import click

from models.common import import_data, export_data


@click.command(name="node")
def node():
    """Docs."""
    click.echo("Node")
    object_name = "network"
    network = import_data(object_name)
    print(network)
