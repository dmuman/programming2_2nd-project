class Node:
    """
    
    """
    def __init__(self, name):
        """
        
        """
        self._name = name
    
    def setName(self, name):
        """
        
        """
        self._name = name

    def getName(self):
        """
        
        """
        return self._name
    
    def __str__(self):
        """
        
        """
        return self._name
    
    def __repr__(self):
        """
        
        """
        return self._name
    
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
        return f'{self._source.getName()} -> {self._destination.getName()}'
    
class WeightedEdge(Edge):
    """
    
    """
    def __init__(self, source, destination, weight = 1.0):
        """
        
        """
        self._source = source
        self._destination = destination
        self._weight = weight

    def setWeight(self, weight):
        """
        
        """
        self._weight = weight

    def getWeight(self):
        """
        
        """
        return self._weight
    
    def __str__(self):
        """
        
        """
        return (f'{self._source.getName()} -> ({self._weight})' + 
                f'{self._destination.getName()}')