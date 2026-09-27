#!/usr/bin/python3
"""
Module 4-print_square
Contains a function that prints a square using the '#' character.
"""


def print_square(size):
    """
    Prints a square with the character # of length size.

    Args:
        size (int): The height and width of the square.

    Raises:
        TypeError: If size is not an integer (or if it is a float < 0).
        ValueError: If size is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
