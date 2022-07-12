#!/usr/bin/python3
"""
function that adds 2 integers
"""


def add_integer(a, b=98):
    """Returns integer sum of 2 numbers"""
    if not type(a) is int:
        if not type(a) is float:
            raise TypeError('a must be an integer')
    if not type(b) is int:
        if not type(b) is float:
            raise TypeError('b must be an integer')

    return int(a) + int(b)
