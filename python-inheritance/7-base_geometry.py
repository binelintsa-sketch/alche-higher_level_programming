#!/usr/bin/python3
"""
Module containing the BaseGeometry class.
"""


class BaseGeometry:
    """A BaseGeometry class."""

    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer strictly greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
