#!/usr/bin/python3
"""Module that contains a function to return the dictionary description of an object."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    """
    return obj.__dict__
