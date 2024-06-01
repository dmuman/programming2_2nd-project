# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

class Digraph:
    """
    A Digraph class
    """
    def __init__(self):
        """
        Initializes the digraph class. Creates a list of nodes 
        and a dictionary of edges where the key is a node in nodes
        and it's value is a list of child nodes with the corresponding
        edge weight.

        Ensures:
        A Digraph object is created with the following attributes:
        self._nodes is a list containing nodes
        where self._nodes = [nodeA, nodeB, ..., nodeN]
        self._edges is a dictionary of edges 
        where self._edges[node] = [(childA, weight), ..., (childN, weight)] 
        """
        self._nodes = []
        self._edges = {}

    def addNode(self, node):
        """
        Appends the list of nodes and updates the dictionary of edges.
        Raises an error, if the node is already in the graph.

        Requires:
        node is of the Node() class with it's name and title,
        graph doesn't already hasve this node.

        Ensures:
        node is added to the graph
        self._nodes = [node, ...]
        an empty list of edges is created for that node
        self._edges[node] = []
        """
        if node in self.getNodes():
            raise ValueError("Duplicate node")
        else:
            self._nodes.append(node)
            self._edges[node] = []

    def addEdge(self, edge):
        """
        Adds a weighted edge to the dictionary of edges
        if both source and destination are in the graph.
        Raises an error otherwise.

        Requires:
        edge is of the WeightedEdge() class
        with its source, destination and weight.
        both source and destination are in graph,
        i.e. self._nodes = [source, destination, ...]

        Ensures:
        an edge is added to the dictionary of edges,
        appending the existing values list of the
        source key,
        i.e. self._edges[source] = [(destination, weight), ...]
        """
        source = edge.getSource()
        destination = edge.getDestination()
        weight = edge.getWeight()
        if source not in self.getNodes():
            raise ValueError("Source not in graph")
        if destination not in self.getNodes():
            raise ValueError("Destination not in graph")
        self._edges[source].append((destination, weight))

    def childrenOf(self, node):
        """
        Returns a list of children of the presented node
        if the node is in the graph (self._nodes).
        Raises an error otherwise.

        Requires:
        node is of the Node() class with its name and title
        and is already in the graph,
        i.e. self._nodes = [node, ...]

        Ensures:
        a list of children of the node,
        i.e. values of the key node in the dictionary
        self._edges

        [(clildA, weight), ..., (childN, weight)]
        """
        if self.hasNode(node):
            return self._edges[node]
        
        raise ValueError("Source not in graph")
    
    def hasNode(self, node):
        """
        Returns true if the presented node is
        already in the graph,
        i.e. self._nodes = [node, ...]

        Requires:
        node is of the Node() class with 
        its name and title.

        Ensures:
        True if node is in self._nodes
        False otherwise
        """
        return node in self.getNodes()
    
    def getNodes(self):
        """
        Returns the list of nodes in the graph.

        Requires:
        Digraph object is initialized.

        Ensures:
        a list that contains all nodes in the graph,
        i.e. self._nodes
        """
        return self._nodes
    
    def getEdges(self):
        """
        Returns the dictionaty of edges in the graph.

        Requires:
        Digraph object is initialized.

        Ensures:
        a dictionary that contains all edges in the graph,
        i.e. self._edges
        """
        return self._edges
    
    def __str__(self):
        """
        A string representation of a graph.

        Requires:
        Digraph object is initialized.

        Ensures:
        A string representation of a graph is printed.
        """
        result = ''
        for source in self._nodes:
            for destination, weight in self._edges[source]:
                result = (f'{result} {source.getName()} ->' +
                          f'{destination.getName()} with weight of {weight} \n')
        return result[:-1]
    
    def __repr__(self):
        """
        A string representation of a graph.

        Requires:
        Digraph object is initialized.

        Ensures:
        A string representation of a graph is printed to the console.
        """
        return self.__str__()