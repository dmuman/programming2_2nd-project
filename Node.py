# 2023-2024 Programacao 2 LTI
# Grupo 31
# 59348 Dmytro Umanskyi
# 62228 Oujie Wu

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
        """
        
        """
        self._title = title

    def getName(self):
        """
        
        """
        return self._name

    def getTitle(self):
        """
        
        """
        return self._title

    def __str__(self):
        """
        
        """
        return self._name
    
    def __repr__(self):
        """
        
        """
        return self.__str__()