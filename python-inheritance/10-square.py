#!/usr/bin/python3
"""
Module containing the Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initializes size after validating it and calls super().__init__().

        Args:
            size (int): The size of the sides of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
