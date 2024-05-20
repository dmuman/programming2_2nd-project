from collections import UserList
from Graphs import *
from NodesEdges import *

class Path(UserList):
    """
    
    """
    def __init__(self):
        self._path = []

    def setPath(self, path):
        """
        
        """
        self._path = path

    def updatePath(self, path):
        """
        
        """
        self._path.append(path)

    def getPath(self):
        """
        
        """
        return self._path

    def DFS(self, graph, start, end, path, shortest, totalDistance = 0.0):
        """
        Requires:
        graph a Digraph;
        start and end nodes;
        path and shortest lists of nodes
        Ensures:
        a shortest path from start to end in graph
        """
        path = path + [start]
        # self.updatePath(start)
        print('Current DFS path:', self.getPath())
        if start == end:
            return path
        for node in graph.childrenOf(start):
            if node not in path: #avoid cycles
                if shortest == None or len(path) < len(shortest):
                    newPath = self.DFS(graph, node, end, path, shortest)
                    if newPath != None:
                        shortest = newPath
        return shortest
    
    def search(self, graph, start, end):
        """
        Requires:
        graph  a Digraph;
        start and end are nodes
        Ensures:
        shortest path from start to end in graph
        """
        return self.DFS(graph, start, end, [], None)
    

    def __str__(self):
        """
        Requires: path a list of nodes
        """
        result = ''
        for i in range(len(self._path)):
            result = result + str(self._path[i])
            if i != len(self._path) - 1:
                result = result + '->'
        return result
    
def testSP():
    nodes = []
    for name in range(6): #Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = Path()
    sp.search(g, nodes[0], nodes[5])
    print('Shortest path found by DFS:', sp)


testSP()