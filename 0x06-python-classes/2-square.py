#!/usr/bin/python3
'''define a class square'''


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
        else if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size:
