# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

class Edge:
    """
        
    """
    def __init__(self, source, destination):
        """
        
        """
        self._source = source
        self._destination = destination

    def setSource(self, source):
        """
        
        """
        self._source = source

    def setDestination(self, destination):
        """
        
        """
        self._destination = destination

    def getSource(self):
        """
        
        """
        return self._source
    
    def getDestination(self):
        """
        
        """
        return self._destination
    
    def __str__(self):
        """
        
        """
        return f'{self._source.getName()} -> {self._destination.getName()}'
    
    def __repr__(self):
        """
        
        """
        return self.__str__()