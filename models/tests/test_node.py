"""Test Identity Class and Functions."""
from faker import Faker
from cryptos import Bitcoin
from models.identity import Identity, Identities
from models.node import Node, Network

faker = Faker()

def test_node():
    """Test creation of node."""
    node = Node(1,9000)
    assert node.name == "nodo1"
    assert str(node) == str({"name": "nodo1", "port": 9000})


def test_empty_network():
    """Test creation of empty network."""
    network = Network()
    assert network is not None


def test_network():
    """Test creation of network."""
    network = Network()
    network.identities.gen_x_identities(5)
    network.gen_x_nodes(3)
    network.create_linear_network()
    assert len(network.identities) == 8
    assert len(network.connections) == 2
