# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

from Digraph import Digraph
from WeightedEdge import WeightedEdge

class Graph(Digraph):
    """
    A Graph class that inherits properties from the Digraph class
    """
    def addEdge(self, edge):
        """
        Overrides already existing method in the Digraph class.
        Adds a reversed weighted edge to the dictionary of edges
        if both source and destination are in the graph.
        Raises an error otherwise.

        Requires:
        edge is of the WeightedEdge() class
        with its source, destination and weight.
        both source and destination are in graph,
        i.e. self._nodes = [source, destination, ...]

        Ensures:
        a reverse edge is added to the dictionary of edges,
        appending the existing values list of the
        source key,
        i.e. self._edges[source] = [(destination, weight), ...]
        and self._edges[destination] = [(source, weight), ...]
        """
        Digraph.addEdge(self, edge)
        reverse = WeightedEdge(edge.getDestination(), edge.getSource(), edge.getWeight())
        Digraph.addEdge(self, reverse)