# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

from infoFromFiles import *
from Path import Path
from sys import argv
import os

here = os.path.dirname(os.path.abspath(__file__))

levadasFile = os.path.join(here, argv[1])
stationsFile = os.path.join(here, argv[2])
outputFile = os.path.join(here, argv[3])

def findNodeByTitle(graph, title):
    """
    A function to find a Node by it's title in the given graph.
    Return a node if found, None otherwise.

    Requires:
    graph is a Graph(),
    title is a title of the Node() that is in the graph.

    Ensures:
    node if its title is found in the given graph,
    None otherwise.
    """
    for node in graph.getNodes():
        if node.getTitle() == title:
            return node
    return None

def safeLevadas(levadasFile, stationsFile, outputFile):
    """
    The main function that runs the whole program. Uses all the previous
    functions and classes methods. Writes a result file to the provided 
    outpuFile name.
    Creates a graph out of all the provided stations in levadasFile,
    pairs of stations from the stationsFile and then finds the best pathes between them.
    At max three pathes for each pair.
    Can be executed from the file of from the console like that:
    'python safeLevadas.py levadasFile stationsFile outputFile'
    
    Requires:
    levadasFile and stationsFile aren's empty.
    levadasFile has the next structure:
    #Id, Name, Connected
    'Id', 'Name', [('otherId', 'time'), ...]
    ...

    stationsFile has the next structure
    'StationA - StationB'
    ...

    Ensures:
    outputFile with the provided name and with the
    results of DFS computations.
    It has the next structure:
    (if the path is found)
    # StartStation - EndStation
    'time', 'path'
    ...
    (if stations don't communicate)
    # StartStation - EndStation
    'StartStation and EndStation do not communicate'
    (if one of the stations are not in the graph)
    # StartStation - EndStation
    'EndStation out of the network'
    """
    graph = readFromNetworkFiles(levadasFile)
    stations = readStations(stationsFile)
    sp = Path()
    linesToWrite = []

    with open(outputFile, 'w') as outFile:
        for startName, endName in stations:
            linesToWrite.append(f'# {startName} - {endName}\n')
            startNode = findNodeByTitle(graph, startName)
            endNode = findNodeByTitle(graph, endName)

            if not startNode or not endNode:
                linesToWrite.append(f'{endName} out of the network\n')            
            else:
                results = sp.search(graph, startNode, endNode)
                if results:
                    for path, time in results:
                        pathTitles = ', '.join(node.getTitle() for node in path)
                        linesToWrite.append(f'{time}, {pathTitles}\n')
                else:
                    linesToWrite.append(f'{startName} and {endName} do not communicate\n')
        for i in range(len(linesToWrite)):
            if i != len(linesToWrite)-1:
                outFile.write(linesToWrite[i])
            else:
                outFile.write(linesToWrite[i].rstrip('\n'))


safeLevadas(levadasFile, stationsFile, outputFile)