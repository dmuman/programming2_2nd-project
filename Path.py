# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

from collections import UserList

class Path(UserList):
    """
    A Path class that inherits properties from the UserList class from the collections library
    """
    def __init__(self):
        """
        Initializes the Path class and its 
        super() class. Creates a bestSolutions attribute
        which is a list.

        Ensures:
        A Path object is created with the following attributes:
        self._bestSolutions that is a list containing the
        three best solutions (paths)
        """
        super().__init__()
        self._bestSolutions = []

    def setBestSolutions(self, bestSolutions):
        """
        Sets the best solutions to the path.

        Requires:
        best solutions is list.

        Ensures:
        self._bestSolutions is updated with the value of
        the new given bestSolutions.
        """
        self._bestSolutions = bestSolutions

    def updateBestSolutions(self, path, time):
        """
        Updates the current 
        best solutions to the problem with the given
        current path and time.
        At maximum, it can append only the three best solutions.

        Requires:
        path is a list representing the sequence of nodes.
        time - is the time accumulated from the weights 
        between each node.

        Ensures:
        self._bestSolutions is appended with the tuples
        of the path and time, then sorted by the time.
        It keeps only three best solutions.
        """
        self._bestSolutions.append((path, time))
        self._bestSolutions.sort(key=lambda x: x[1])
        if len(self._bestSolutions) > 3:
            self._bestSolutions = self._bestSolutions[:3]

    def getBestSolutions(self):
        """
        Returns the best solutions.

        Requires:
        Path object is initialized.

        Ensures:
        a list that represents the best solutions found.
        i.e. self._bestSolutins
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
        A string representation of a path.

        Requires:
        Path object is initialized.

        Ensures:
        A string representation of a path is printed.
        """
        result = ''
        for i in range(len(self._path)):
            result = result + str(self._path[i])
            if i != len(self._path) - 1:
                result = result + '->'
        return result
    
    def __repr__(self):
        """
        A string representation of a path.

        Requires:
        Path object is initialized.

        Ensures:
        A string representation of a path is printed to the console.
        """
        return self.__str__()