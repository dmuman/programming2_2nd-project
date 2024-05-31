# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

from Digraph import Digraph
from WeightedEdge import WeightedEdge

class Graph(Digraph):
    """
    
    """
    def addEdge(self, edge):
        """
        
        """
        Digraph.addEdge(self, edge)
        reverse = WeightedEdge(edge.getDestination(), edge.getSource(), edge.getWeight())
        Digraph.addEdge(self, reverse)