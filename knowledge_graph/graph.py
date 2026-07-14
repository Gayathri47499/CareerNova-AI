import networkx as nx


class CareerGraph:

    def __init__(self):

        self.graph = nx.DiGraph()

    def add_node(self, node):

        self.graph.add_node(node)

    def add_edge(self, source, relation, target):

        self.graph.add_edge(

            source,

            target,

            relation=relation

        )