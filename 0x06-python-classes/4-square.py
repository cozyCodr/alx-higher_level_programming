#!/usr/bin/python3
"""define a class square"""


class Square:
    """square attributes"""

    def __init__(self, size=0):
        """
        Initialization of the square
        Args:
            size (int): Initial Size of the Square

        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Size Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for private property size"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns area of square"""
        return self.__size ** 2
