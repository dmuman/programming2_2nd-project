class Node:
    """
    
    """
    def __init__(self, name, title):
        """
        
        """
        self._name = name
        self._title = title
    
    def setName(self, name):
        """
        
        """
        self._name = name

    def setTitle(self, title):
        self._title = title

    def getName(self):
        """
        
        """
        return self._name

    def getTitle(self):
        return self._title

    def __str__(self):
        """
        
        """
        return str((self._name, self._title))
    
    def __repr__(self):
        """
        
        """
        return self.__str__()
    
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
    def __init__(self, source, destinationWeight):
        """
        
        """
        super().__init__(source, destinationWeight[0])
        self._weight = destinationWeight[1]

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
    
    def __repr__(self):
        """
        
        """
        return self.__str__()