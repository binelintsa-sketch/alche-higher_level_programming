#!/usr/bin/python3
"""
Module that defines a Rectangle class with printable string representation.
"""


class Rectangle:
    """Class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the current rectangle perimeter.

        Returns 0 if width or height is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the rectangle using #.

        Returns an empty string if width or height is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)
        return "\n".join(rect_str)
