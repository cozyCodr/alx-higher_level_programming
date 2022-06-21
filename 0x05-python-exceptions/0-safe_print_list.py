#!/usr/bin/python3

"""
Write a function that prints x elements of a list
"""


def safe_print_list(my_list=[], x=0):
    my_string = ""
    new_list = my_list[:]
    try:
        for i in range(x):
            my_string = my_string + str(new_list[i])
        return int(my_string)
    except IndexError:
        return int(my_string)
