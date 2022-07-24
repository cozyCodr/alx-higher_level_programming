#!/usr/bin/python3
"""divides matrix"""


def matrix_divided(matrix, div):
    """divides all elements of matrix"""

    # Matrix should always be a list
    if not type(matrix) is list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Matrix should have length of at least 1
    if len(matrix) < 1:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if matrix contains lists only
    for inner in matrix:
        if not type(inner) is list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if list are of the same length
    list_len = len(matrix[0])
    for inner in matrix:
        if len(inner) != list_len:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if all elements are of type
    for inner in matrix:
        for element in inner:
            if not type(element) is float:
                if not type(element) is int:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

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


def main():
    mylist = [[2, 4, 6], [3, 2, 1]]

    new_list = matrix_divided([[2.2, 0.2], [3, 2, 1]], 3)

    print(new_list)


if __name__ == "__main__":
    main()
