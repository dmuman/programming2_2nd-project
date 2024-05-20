from NodesEdges import Edge

class Digraph:
    """
    
    """
    def __init__(self):
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
        if not (source in self._nodes and destination in self._nodes):
            raise ValueError("Node not in graph")
        self._edges[source].append(destination)

    def childrenOf(self, node):
        """
        
        """
        return self._edges[node]
    
    def edgesFrom(self, node):
        """
        
        """
        return self._edges[node]
    
    def hasNode(self, node):
        """
        
        """
        return node in self._nodes
    
    def getNodes(self):
        return self._nodes
    
    def __str__(self):
        """
        
        """
        result = ''
        for source in self._nodes:
            for destination in self._edges[source]:
                result = (result + source.getName() + '->' 
                          + destination.getName() + '\n')
        return result[:-1]
    
    def __repr__(self):
        """
        
        """
        result = ''
        for source in self._nodes:
            for destination in self._edges[source]:
                result = (result + source.getName() + '->' 
                          + destination.getName() + '\n')
        return result[:-1]
        
class Graph(Digraph):
    """
    
    """
    def addEdge(self, edge):
        """
        
        """
        Digraph.addEdge(self, edge)
        reverse = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, reverse)