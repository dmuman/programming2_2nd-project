# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

from Node import Node
from Graph import Graph
from WeightedEdge import WeightedEdge

def readFromNetworkFiles(filename):
    """
    
    """
    graph = Graph()
    nodes = {}

    with open(filename, 'r', encoding='utf-8-sig') as inFile:
        lines = inFile.readlines()

        for line in lines[1:]:  # skip the header
            line = line.strip()
            if line:
                linesInfo = line.split(", ", 2)  # split only on the first two commas
                if len(linesInfo) == 3:
                    id, name, connected = linesInfo
                    connected = connected.strip("[]")  # remove the square brackets

                    if id not in nodes:
                        node = Node(id, name)
                        nodes[id] = node
                        graph.addNode(node)
                    else:
                        nodes[id].setTitle(name)

                    source = nodes[id]

                    if connected:
                        connections = connected.split("), (")
                        for connection in connections:
                            connection = connection.strip("()")  # remove parentheses
                            children, time = connection.split(", ")
                            time = int(time)

                            if children not in nodes:
                                childNode = Node(children, "")
                                nodes[children] = childNode
                                graph.addNode(childNode)

                            destination = nodes[children]
                            edge = WeightedEdge(source, destination, time)
                            graph.addEdge(edge)

    return graph

def readStations(filename):
    """
    
    """
    stations = []
    with open(filename, 'r', encoding='utf-8-sig') as inFile:
        lines = inFile.readlines()

        for line in lines:
            line = line.strip()
            if line:
                start, end = line.split(" - ")
                stations.append((start, end))

    return stations