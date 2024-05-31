# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

from collections import UserList

class Path(UserList):
    """
        
    """
    def __init__(self):
        """
        
        """
        super().__init__()
        self._bestSolutions = []

    def setBestSolutions(self, bestSolutions):
        """
        
        """
        self._bestSolutions = bestSolutions

    def updateBestSolutions(self, path, time):
        """
        
        """
        self._bestSolutions.append((path, time))
        self._bestSolutions.sort(key=lambda x: x[1])
        if len(self._bestSolutions) > 3:
            self._bestSolutions = self._bestSolutions[:3]

    def getBestSolutions(self):
        """
        
        """
        return self._bestSolutions

    def DFS(self, graph, start, end, path, totalTime=0):
        """
        
        """
        path = path + [start]
        if start == end:
            self.updateBestSolutions(path, totalTime)
            return

        for node, time in graph.childrenOf(start):
            if node not in path:  # avoid cycles
                newTime = totalTime + time
                self.DFS(graph, node, end, path, newTime)
    
    def search(self, graph, start, end):
        """
        
        """
        self.setBestSolutions([])  # Clear previous solutions
        self.DFS(graph, start, end, [], 0)
        return self.getBestSolutions()

    def __str__(self):
        """
        
        """
        result = ''
        for i in range(len(self._path)):
            result = result + str(self._path[i])
            if i != len(self._path) - 1:
                result = result + '->'
        return result
    
    def __repr__(self):
        """
        
        """
        return self.__str__()