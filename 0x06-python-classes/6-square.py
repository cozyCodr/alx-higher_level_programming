#!/usr/bin/python3
"""define a class square"""


class Square:
    """square attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization of the square
        Args:
            size (int): Initial Size of the Square
            position (tuple): contains number of spaces
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if (not type(position[0]) is int) or (not type(position[1]) is int):
            raise TypeError("position must be a tuple of positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of positive integers")
        else:
            self.__position = position

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
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """fills position with spaces"""
        if (not type(value[0]) is int) or (not type(value[1]) is int):
            if value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of positive integers")
            else:
                self.__position = value

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints positioned square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for y in range(self.__position[0]):
                    print("_", end="")
                for x in range(self.__size):
                    if x == (self.__size - 1):
                        print("#")
                    else:
                        print("#", end="")
