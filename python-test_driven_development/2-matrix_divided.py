#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide the elements by.

    Returns:
        A new matrix with all elements divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows of matrix are not all of the same size,
                   or if div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg_type)
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(msg_type)

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
