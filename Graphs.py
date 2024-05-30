from NodesEdges import Edge, WeightedEdge

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
            # self._edges.append(Edge(node, ))

    def addEdge(self, edge):
        """
        Edge is a WeightedEdge
        """
        source = edge.getSource()
        destination = edge.getDestination()
        weight = edge.getWeight()
        if not (source in self._nodes and destination in self._nodes):
            raise ValueError("Node not in graph")
        self._edges[source].append([destination, weight])
        # self._edges.append()

    def childrenOf(self, node):
        """
        
        """
        # for child in self._edges[node]:
        #     return child[0]
        return self._edges[node]
    
    def weightOfEdge(self, node):
        for child in self._edges[node]:
            return child[1]
        # return self._nodes[node][1]

    
    def hasNode(self, node):
        """
        
        """
        return node in self._nodes
    
    def getNodes(self):
        return self._nodes
    
    def getEdges(self):
        return self._edges
    
    def __str__(self):
        """
        
        """
        result = ''
        for source in self._nodes:
            for destination, weight in self._edges[source]:
                result = (f'{result} {source.getName()} -> {destination.getName()} with weight of {weight} \n')
        return result[:-1]
    
    def __repr__(self):
        """
        
        """
        return self.__str__()
        
class Graph(Digraph):
    """
    
    """
    def addEdge(self, edge):
        """
        
        """
        Digraph.addEdge(self, edge)
        reverse = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, reverse)