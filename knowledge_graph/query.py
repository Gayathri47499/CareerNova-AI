class GraphQuery:

    def __init__(self, graph):

        self.graph = graph

    def nodes(self):

        return list(

            self.graph.graph.nodes()

        )