#!/usr/bin/python3
"""
prints a 2 dimensional matrix
"""


def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        if len(matrix) == 1:
            for inner in matrix:
                for x in inner:
                    print("{:d}".format(x), end="")
        else:
            for inner in matrix:
                for x in inner:
                    if inner.index(x) == (len(inner) - 1):
                        print("{:d}".format(x))
                    else:
                        print("{:d}".format(x), end=" ")
    elif isinstance(matrix, str):
        new_matrix = [*matrix]
        print("{}".format("".join(new_matrix)))
