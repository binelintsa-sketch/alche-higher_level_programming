#!/usr/bin/python3
"""
Module containing the MyList class that inherits from list.
"""


class MyList(list):
    """A custom list class extending Python's built-in list."""

    def print_sorted(self):
        """Prints the list elements sorted in ascending order."""
        print(sorted(self))
