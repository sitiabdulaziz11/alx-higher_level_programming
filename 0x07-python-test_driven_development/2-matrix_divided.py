#!/usr/bin/python3
"""
A module that divides all elements of a matrix
return a new matrix
"""

def matrix_divided(matrix, div):
    """
    function divide matrix list
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(val, (int, float)) for row in matrix for val in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    rl = len(matrix[0])
    if not all(len(row) == rl for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    div_matrix = [[round(item / div, 2) for item in row] for row in matrix]
    return div_matrix
