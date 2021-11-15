"""Class Node"""
from models.blockchain import Blockchain
from models.identity import Identities

class Node:
    """class Node."""

    def __init__(self, node_id, port, ledger=Blockchain()):
        """Init."""
        self.node_id = node_id
        self.port = port
        self.ledger = ledger
        self.name = f"nodo{node_id}"

    def __str__(self):
        """String method."""
        return str(self.to_dict())

    def to_dict(self):
        """Convert in dict."""
        return {"name": self.name, "port": self.port}


def run_node(name):
    """Prende un nodo y pone a escuchar y a enviar mensajes."""
    print(name)


class Network:
    """Class Network."""

    def __init__(self, identities: Identities=Identities()):
        """Init."""
        self.nodes = []
        self.connections = []
        self.identities = identities


    def __str__(self):
        """String method."""
        return str(self.to_dict())


    def to_dict(self):
        """To dict method."""
        return {
            "nodes": [node.to_dict() for node in self.nodes],
            "connections": self.connections,
            "identities": [str(identity) for identity in self.identities.identities],
            }


    def read_network_file(self):
        """Read Network file."""


    def gen_x_nodes(self, num):
        """Return a list of objects."""
        port_base = 9000
        for i in range(num):
            node = Node(i, port_base+i)
            self.nodes.append(node)
            email = f"{node.name}@example.com"
            self.identities.gen_identity(node.name, email)


    def create_linear_network(self):
        """Create a linear network."""
        for i in range(len(self.nodes)-1):
            pair = (self.nodes[i].name,self.nodes[i+1].name)
            self.connections.append(pair)
