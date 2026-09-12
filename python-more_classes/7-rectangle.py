#!/usr/bin/python3
"""
Module that defines a Rectangle class with customizable print symbol.
"""


class Rectangle:
    """Class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Return the printable representation using print_symbol.

        Returns an empty string if width or height is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        rect_str = []
        for i in range(self.__height):
            rect_str.append(symbol * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """Return a string representation of the rectangle to recreate it.

        Format: Rectangle(width, height)
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message and decrement count when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
