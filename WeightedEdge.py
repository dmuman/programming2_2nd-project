# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

from Edge import Edge

class WeightedEdge(Edge):
    """
    A WeightedEdge class that inherits properties from the Edge class
    """
    def __init__(self, source, destination, weight):
        """
        Initializes the WeightedEdge class and its 
        super() class with
        the given source, destination and weight.

        Requires:
        source and destination are of the Node() class
        with its name and title
        weight is a positive int.

        Ensures:
        A WeightesEdge object is created with the following attributes:
        self._source, self._destination and self._weight that are equal 
        to the given source, destination and weight.
        """
        super().__init__(source, destination)
        self._weight = weight

    def setWeight(self, weight):
        """
        Updates the weight between source and destination
        with the given new weight.

        Requires:
        weight is a positive int.

        Ensures:
        self._source is updated with the value of
        the new given source.
        """
        self._weight = weight

    def getWeight(self):
        """
        Returns the weight of the WeightedEdge.

        Requires:
        WeightedEdge object is initialized.

        Ensures:
        a int that represents the weight of the edge
        i.e. self._weight
        """
        return self._weight
    
    def __eq__(self, other):
        """
        Compares two WeightedEdges by its source, destination and weight.

        Requires:
        WeightedEdge object is initialized.
        other is a WeightedEdge object with its source, destination and weight.

        Ensures:
        True if the two WeightedEdges are equal by there three parameters,
        False otherwise.
        """
        return (self.getSource() == other.getSource() and
                self.getDestination() == other.getDestination() and
                self.getWeight() == other.getWeight())
    
    def __lt__(self, other):
        """
        Compares two WeightedEdges by its weight.

        Requires:
        WeightedEdge object is initialized.
        other is a WeightedEdge object with its weight.

        Ensures:
        True if the two WeightedEdge's weight is less than other's weight,
        False otherwise.
        """
        return self.getWeight() < other.getWeight()
    
    def __str__(self):
        """
        A string representation of a weighted edge.

        Requires:
        WeightedEdge object is initialized.

        Ensures:
        A string representation of a weighted edge is printed.
        """
        return f'{self._source.getName()} -> ({self._weight}) {self._destination.getName()}'
    
    def __repr__(self):
        """
        A string representation of a weighted edge.

        Requires:
        WeightedEdge object is initialized.

        Ensures:
        A string representation of a weighted edge is printed to the console.
        """
        return self.__str__()