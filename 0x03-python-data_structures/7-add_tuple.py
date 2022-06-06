#!/usr/bin/python3
"""
add the contents of 2 tuples
"""


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        return tuple([int(tuple_a[0]) + int(tuple_b[0]),
                     int(tuple_a[1]) + int(tuple_b[1])])
    elif len(tuple_a) >= 2 and len(tuple_b) < 2:
        if len(tuple_b) == 1:
            return tuple([int(tuple_a[0]) + int(tuple_b[0]),
                          int(tuple_a[1]) + 0])
        if len(tuple_b) == 0:
            return tuple_a
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        return tuple([int(tuple_a[0]) + int(tuple_b[0]), 0])
    elif len(tuple_b) >= 2 and len(tuple_a) < 2:
        if len(tuple_a) == 1:
            return tuple([int(tuple_a[0]) + int(tuple_b[0]), int(tuple_b[1])])
        if len(tuple_a) == 0:
            return tuple_b
