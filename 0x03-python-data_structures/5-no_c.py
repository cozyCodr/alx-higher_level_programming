#!/usr/bin/python3
"""
removes all instances of c and C in String
"""


def no_c(my_string):
    new_string = [x for x in my_string if x != 'c' and x != 'C']
    return "".join(new_string)
