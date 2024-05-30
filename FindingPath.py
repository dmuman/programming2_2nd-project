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

    # def DFS(self, graph, start, end, path, shortest, totalDistance = 0.0):
    #     """
    #     Requires:
    #     graph a Digraph;
    #     start and end nodes;
    #     path and shortest lists of nodes
    #     Ensures:
    #     a shortest path from start to end in graph
    #     """
    #     path = path + [start]
    #     # for node in path:
    #     #     print(type(node))
    #     print(path)
    #     print('Current DFS path:', [str(node) for node in path], 'with total distance:', totalDistance)
    #     if start == end:
    #         return path, totalDistance
    #     # bestDistance = 0.0
    #     for node, distance in graph.childrenOf(start):
    #             print(f'children: {node}, dist: {distance}')
    #         # edge = WeightedEdge()
    #             if node not in path: #avoid cycles
    #                 newDistance = totalDistance + distance
    #                 print(newDistance)
    #                 print('short', shortest)
    #                 if shortest == None or newDistance < shortest[1]:
    #                 # if shortest == None or len(path) < len(shortest):
    #                     print('shortest', shortest)
    #                     newPath, newTotalDistance = self.DFS(graph, node, end, path, shortest, newDistance)
    #                     if newPath != None:
    #                         shortest = (newPath, newTotalDistance)
    #                         # print('shortest', shortest)
    #     return shortest
    #     # TODO
    #     # the problem is now here
    #     # edge is not the Edge, but two nodes from
    #     # the Digraph class.
    #     # we need to figure out how to change that
    #     # for edge in graph.edgesFrom(start):
    #     #     print(type(edge))
    #     #     node = edge.getDestination()
    #     #     if node not in path:  # avoid cycles
    #     #         distance = totalDistance + edge.getWeight()
    #     #         if shortest is None or distance < shortest[1]:
    #     #             newPath, newDistance = self.DFS(graph, node, end, path, shortest, distance)
    #     #             if newPath is not None:
    #     #                 shortest = (newPath, newDistance)
    #     # return shortest

    def DFS(self, graph, start, end, path, shortest, totalDistance=0.0):
        """
        Requires:
        graph a Digraph;
        start and end nodes;
        path and shortest lists of nodes
        Ensures:
        a shortest path from start to end in graph
        """
        path = path + [start]
        # print(path)
        print('Current DFS path:', [str(node) for node in path], 'with total distance:', totalDistance)
        
        if start == end:
            return path, totalDistance

        for node, distance in graph.childrenOf(start):
            # print(f'children: {node}, dist: {distance}')
            if node not in path:  # avoid cycles
                newDistance = totalDistance + distance
                # print(newDistance)
                # print('short', shortest)
                if shortest is None or newDistance < shortest[1]:
                    # print('shortest', shortest)
                    result = self.DFS(graph, node, end, path, shortest, newDistance)
                    if result is not None:
                        newPath, newTotalDistance = result
                        shortest = (newPath, newTotalDistance)
        
        return shortest
    
    def search(self, graph, start, end):
        """
        Requires:
        graph  a Digraph;
        start and end are nodes
        Ensures:
        shortest path from start to end in graph
        """
        shortest = self.DFS(graph, start, end, [], None, 0.0)
        if shortest:
            self.setPath(shortest[0])
        return shortest
    

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
    for name in range(6):  # Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(WeightedEdge(nodes[0], nodes[1], 5))
    g.addEdge(WeightedEdge(nodes[1], nodes[2], 4))
    g.addEdge(WeightedEdge(nodes[2], nodes[3], 9))
    g.addEdge(WeightedEdge(nodes[2], nodes[4], 7))
    g.addEdge(WeightedEdge(nodes[3], nodes[4], 3))
    g.addEdge(WeightedEdge(nodes[3], nodes[5], 2))
    g.addEdge(WeightedEdge(nodes[0], nodes[2], 10))
    g.addEdge(WeightedEdge(nodes[1], nodes[0], 3))
    g.addEdge(WeightedEdge(nodes[3], nodes[1], 1))
    g.addEdge(WeightedEdge(nodes[4], nodes[0], 8))

    sp = Path()
    result = sp.search(g, nodes[0], nodes[5])
    if result:
        print('Shortest path found by DFS:', sp)
    else:
        print('No path found')

    # print(g)
    # print(g._edges)

    # # for g in g.getNodes():
    # #     print(type(g))
    # # for node in nodes:
    # #     print(type(node))

    # for edge in g.getEdges():
    #     print(edge)


testSP()