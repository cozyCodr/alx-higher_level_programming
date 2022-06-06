#!/usr/bin/python3
"""
removes all instances of c and C in String
"""


def no_c(my_string):
    new_string = list(my_string)
    for i in new_string:
        index = new_string.index(i)
        if i == 'c' or i == 'C':
            new_string.pop(i)
    return "".join(new_string)
