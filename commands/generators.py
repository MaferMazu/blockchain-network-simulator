"""Commands to generate identities, nodes and transactions."""

import click

from models.common import import_data, export_data
from models.node import Network


@click.command(name="genTransac")
def gen_transac():
    """Docs."""
    click.echo("genTransac")


@click.command(name="genIdenti")
@click.option("-i","identities", default=3, type=int, help="number of identities to generate")
@click.option("-n","nodes", default=3, type=int, help="number of nodes to generate")
def gen_identi(identities, nodes):
    """Generate identities and nodes."""

    network = Network()
    network.identities.gen_x_identities(identities)
    network.gen_x_nodes(nodes)
    network.create_linear_network()
    export_data("network", network)
    click.echo(f">> {identities} identities and {nodes} nodes have been generated in linear network.")
