#!/usr/bin/python3
"""divides matrix"""


def matrix_divided(matrix, div):
    """divides all elements of matrix"""

    # Long Error messages
    type_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Matrix should always be a list
    if not type(matrix) is list:
        raise TypeError(type_msg)

    # Matrix should have length of at least 1
    if len(matrix) < 1:
        raise TypeError(type_msg)

    # Check if matrix contains lists only
    for inner in matrix:
        if not type(inner) is list:
            raise TypeError(type_msg)

    # Check if list are of the same length
    list_len = len(matrix[0])
    for inner in matrix:
        if len(inner) != list_len:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if all elements are of type
    for inner in matrix:
        for element in inner:
            if type(element) is float:
                pass
            elif type(element) is int:
                pass
            else:
                raise TypeError(type_msg)

    # Make sure div is a number
    if not type(div) is float:
        if not type(div) is int:
            raise TypeError("div must be a number")

    # Make sure div isn't zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # No errors raise, proceed with division
    new_matrix = []
    for inner in matrix:
        temp = []
        for elem in inner:
            temp.append(round((elem / div), 2))

        new_matrix.append(temp)

    return new_matrix

