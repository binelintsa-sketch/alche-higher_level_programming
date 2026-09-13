#!/usr/bin/python3
"""
Module containing the inherits_from function.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class inherited from a class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj's class inherited from a_class (and is not a_class itself);
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

