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
    
    """
    for node in graph.getNodes():
        if node.getTitle() == title:
            return node
    return None

def safeLevadas(levadasFile, stationsFile, outputFile):
    """
    
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