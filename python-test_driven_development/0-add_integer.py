#!/usr/bin/python3
"""
Module 0-add_integer
Contains a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting floats to integers.

    Args:
        a: First parameter (integer or float).
        b: Second parameter (integer or float, defaults to 98).

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
