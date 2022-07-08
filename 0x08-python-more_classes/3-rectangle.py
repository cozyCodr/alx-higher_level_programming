#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """defines rectangle class"""
    def __init__(self, width=0, height=0):
        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def print(self):
        for x in range(self.__height):
            for i in range(self.__width):
                if i == (self.__width - 1):
                    if x == self.__height - 1:
                        print("#", end="")
                    else:
                        print("#")
                else:
                    print("#", end="")
        return ""

    def __str__(self):
        return str(self.print())
