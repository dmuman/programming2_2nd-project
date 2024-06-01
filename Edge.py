# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

class Edge:
    """
    An Edge class
    """
    def __init__(self, source, destination):
        """
        Initializes the Edge class with the given source and destination.

        Requires:
        source and destination are of the Node() class
        with its name and title.

        Ensures:
        An Edge object is created with the following attributes:
        self._source and self._destination that are equal 
        to the given source and destination.
        """
        self._source = source
        self._destination = destination

    def setSource(self, source):
        """
        Updates the source node with the new given
        source.

        Requires:
        source is of the Node() class with
        its name and title.

        Ensures:
        self._source is updated with the value of
        the new given source.
        """
        self._source = source

    def setDestination(self, destination):
        """
        Updates the destination node with the new given
        destination.

        Requires:
        destination is of the Node() class with
        its name and title.

        Ensures:
        self._destination is updated with the value of
        the new given destination.
        """
        self._destination = destination

    def getSource(self):
        """
        Returns the source of the Edge.

        Requires:
        Edge object is initialized.

        Ensures:
        a Node() object that represents the source of the edge
        i.e. self._source
        """
        return self._source
    
    def getDestination(self):
        """
        Returns the destination of the Edge.

        Requires:
        Edge object is initialized.

        Ensures:
        a Node() object that represents the destination of the edge
        i.e. self._destination
        """
        return self._destination
    
    def __eq__(self, other):
        """
        Compares two Edges by its source and destination.

        Requires:
        Edge object is initialized.
        other is an Edge object with its source and destination.

        Ensures:
        True if the two Edges are equal by there two parameters,
        False otherwise.
        """
        return (self.getSource() == other.getSource() and 
                self.getDestination() == other.getDestination())
    
    def __str__(self):
        """
        A string representation of an edge.

        Requires:
        Edge object is initialized.

        Ensures:
        A string representation of an edge is printed.
        """
        return f'{self._source.getName()} -> {self._destination.getName()}'
    
    def __repr__(self):
        """
        A string representation of an edge.

        Requires:
        Edge object is initialized.

        Ensures:
        A string representation of an edge is printed to the console.
        """
        return self.__str__()