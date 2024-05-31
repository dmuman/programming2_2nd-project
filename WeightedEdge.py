# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

from Edge import Edge

class WeightedEdge(Edge):
    """
        
    """
    def __init__(self, source, destination, weight):
        """
        
        """
        super().__init__(source, destination)
        self._weight = weight

    def setWeight(self, weight):
        """
        
        """
        self._weight = weight

    def getWeight(self):
        """
        
        """
        return self._weight
    
    def __eq__(self, other):
        """
        
        """
        return self.getSource() == other.getSource() and\
            self.getDestination() == other.getDestination() and\
            self.getWeight() == other.getWeight()
    
    def __lt__(self, other):
        """
        
        """
        return self.getWeight() < other.getWeight()
    
    def __str__(self):
        """
        
        """
        return f'{self._source.getName()} -> ({self._weight}) {self._destination.getName()}'
    
    def __repr__(self):
        """
        
        """
        return self.__str__()