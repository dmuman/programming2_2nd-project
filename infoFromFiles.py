# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

from Node import Node
from Graph import Graph
from WeightedEdge import WeightedEdge

def readFromNetworkFiles(filename):
    """
    Reads the network file, that contains information
    about all the existing stations 
    (i.e. its ids, names and to which stations they 
    are connected and the time ti travel between them)
    Returns a graph object created with that information.

    Requires:
    filename is a string that represents the network file name and
    has .txt at the end. The file itself is not empty
    and contains a header (#Id, Name, Connected:)
    Each station is like the following:
    'Id, name, [(otherStationId, timeToTravelBetweenStations)]'
    
    Ensures:
    a Graph object is created with the nodes and edges,
    where each node is equal to Node(Id, name) and 
    each edge is a weighted edge that is equal to
    WeightedEdge(sourceNode, destinationNode, time)
    """
    graph = Graph() # initislizing Graph object, so the edges can be reversed
    nodes = {}

    with open(filename, 'r', encoding='utf-8-sig') as inFile:
        lines = inFile.readlines()

        for line in lines[1:]:  # skipping the header
            line = line.strip()
            if line:
                linesInfo = line.split(", ", 2)  # splitting only on the first two commas
                if len(linesInfo) == 3:
                    id, name, connected = linesInfo
                    connected = connected.strip("[]")  # removing the square brackets

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
                            connection = connection.strip("()")  # removing parentheses
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
    Reads the stations file, that contains information
    about stations the program need to find connection between. 
    (i.e. its names(titles))
    Returns a list that contains stations' names (titles)

    Requires:
    filename is a string that represents the stations file name and
    has .txt at the end. The file itself is not empty
    Each pair of stations' names is like the following:
    'stationName - otherStationName'
    
    Ensures:
    a list containing tuples with the names of stations
    with the next structure:
    [(stationNameA - otherStationNameA), ..., (stationNameN - otherStationNameN)]
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