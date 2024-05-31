# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

class Digraph:
    """
    
    """
    def __init__(self):
        """
        
        """
        self._nodes = []
        self._edges = {}

    def addNode(self, node):
        """
        
        """
        if node in self._nodes:
            raise ValueError("Duplicate node")
        else:
            self._nodes.append(node)
            self._edges[node] = []

    def addEdge(self, edge):
        """
        
        """
        source = edge.getSource()
        destination = edge.getDestination()
        weight = edge.getWeight()
        if source not in self._nodes:
            raise ValueError("Source not in graph")
        if destination not in self._nodes:
            raise ValueError("Destination not in graph")
        self._edges[source].append((destination, weight))

    def childrenOf(self, node):
        """
        
        """
        return self._edges[node]
    
    def hasNode(self, node):
        """
        
        """
        return node in self._nodes
    
    def getNodes(self):
        """
        
        """
        return self._nodes
    
    def getEdges(self):
        """
        
        """
        return self._edges
    
    def __str__(self):
        """
        
        """
        result = ''
        for source in self._nodes:
            for destination, weight in self._edges[source]:
                result = (f'{result} {source.getName()} ->' +
                          f'{destination.getName()} with weight of {weight} \n')
        return result[:-1]
    
    def __repr__(self):
        """
        
        """
        return self.__str__()