# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

class Node:
    """
    A Node class 
    """
    def __init__(self, name, title):
        """
        Initializes the node class.

        Requires:
        name and title are string.

        Ensures:
        A Node object is created with the following attributes:
        self._name and self._title that are equal 
        to the given name and title.
        """
        self._name = name
        self._title = title

    def setName(self, name):
        """
        Updates the name with the new given
        name.

        Requires:
        name is string

        Ensures:
        self._name is updated with the value of
        the new given name.
        """
        self._name = name

    def setTitle(self, title):
        """
        Updates the title with the new given
        title.

        Requires:
        title is string

        Ensures:
        self._title is updated with the value of
        the new given title.
        """
        self._title = title

    def getName(self):
        """
        Returns the name of the Node.

        Requires:
        Node object is initialized.

        Ensures:
        a name of the node is returned.
        i.e. self._names
        """
        return self._name

    def getTitle(self):
        """
        Returns the title of the Node.

        Requires:
        Node object is initialized.

        Ensures:
        a title of the node is returned.
        i.e. self._titles
        """
        return self._title

    def __str__(self):
        """
        A string representation of a node.

        Requires:
        Node object is initialized.

        Ensures:
        A string representation of a node is printed.
        """
        return self._name
    
    def __repr__(self):
        """
        A string representation of a node.

        Requires:
        Node object is initialized.

        Ensures:
        A string representation of a node is printed to the console.
        """
        return self.__str__()