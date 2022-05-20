#!/usr/bin/python3
""" matrix_divided divides the given matrix
by the parameter "div", and returns the divided matrix
"""


def matrix_divided(matrix, div):
    """[summary]

    Args:
        matrix ([type]): [description]
        div ([type]): [description]

    Raises:
        TypeError: [description]
        ZeroDivisionError: [description]
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    res_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)",
                    " of integers/floats")
            else:
                inner_list.append(round(items / div, 2))
        res_matrix.append(inner_list)

    return res_matrix
