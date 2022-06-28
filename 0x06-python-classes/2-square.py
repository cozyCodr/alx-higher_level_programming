#!/usr/bin/python3
"""square class defined by size"""


class Square:
    """class that defines a square"""
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
