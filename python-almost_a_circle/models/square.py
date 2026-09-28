#!/usr/bin/python3
"""
Module models/square
Defines the Square class inheriting from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class representing a square shape.
    Inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): Size of the square's sides (> 0).
            x (int, optional): Horizontal position offset (>= 0).
            y (int, optional): Vertical position offset (>= 0).
            id (int, optional): Identifier for the instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size (sets both width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """
        Updates attributes of the Square instance.

        Args:
            *args: Position arguments (id, size, x, y).
            **kwargs: Key/value arguments corresponding to attributes.
        """
        attributes = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
