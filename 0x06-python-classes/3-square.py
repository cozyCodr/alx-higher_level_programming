#!/usr/bin/python3
"""define a class square"""


class Square:
    """square attributes"""

    def __init__(self, size=0):
        """
        Iniitialization of the square
        Args:
            size (int): Initial Size of the Square

        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size ** 2
