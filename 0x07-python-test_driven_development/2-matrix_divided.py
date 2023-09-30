#!/usr/bin/python3
"""
A module that divides all elements of a matrix
return a new matrix
"""


def matrix_divided(matrix, div):
    """
    function divide matrix list
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        if div == 0:
            raise ZeroDivisionError("division by zero")
    div_matrix = [[round(item / div, 2) for item in row] for row in matrix]
    return div_matrix
