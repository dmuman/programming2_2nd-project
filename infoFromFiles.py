from NodesEdges import *
from Graphs import *

def readFromNetworkFiles(filename):
    with open(filename, 'r', encoding='utf-8-sig') as inFile:
        lines = inFile.readlines()
        
        data = []
        for line in lines[1:]:  # skip the header
            line = line.strip()
            if line:
                parts = line.split(", ", 2)  # split only on the first two commas
                if len(parts) == 3:
                    id, name, connected = parts
                    connected = connected.strip("[]")  # remove the square brackets
                    connectedList = []
                    
                    # Manually parse the connected_str to extract tuples
                    if connected:
                        connections = connected.split("), (")
                        for connection in connections:
                            connection = connection.strip("()")  # remove parentheses
                            children, distance = connection.split(", ")
                            connectedList.append((children, int(distance)))
                    
                    data.append([id, name, connectedList])
        
        return data


nodes = []
connectedList = []
g = Digraph()
for data in readFromNetworkFiles('myLevadasNetwork.txt'):
    # dataLst = list(data[2])
    # print(data)
    # print(dataLst)
    name, title, connected = data
    nodes.append(Node(name, title))
    connectedList.append(connected)
    # print(name, title, connectedList)

for n in nodes:
    g.addNode(n)

for i in range(len(connectedList)):
    print(connectedList[i])
    g.addEdge(WeightedEdge(nodes[i], ))

# print(connectedList)
# print(nodes)
# print(g)

class Network():
    """
    
    """

    def __init__(self, id, name, connected):
        self._idName = {}
        self._idName[id] = name