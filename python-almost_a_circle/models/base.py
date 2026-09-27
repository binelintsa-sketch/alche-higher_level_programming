#!/usr/bin/python3
"""
Module models/base
Defines the Base class for the project.
"""
import json


class Base:
    """
    Base class for managing id attribute in all future classes
    and handling serialization/deserialization tasks.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int, optional): Identifier for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation, or "[]" if None/empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances inheriting from Base.
        """
        filename = "{}.json".format(cls.__name__)
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_str = cls.to_json_string(list_dicts)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by the JSON string json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: List represented by json_string, or [] if None/empty.
        """
        if json_string is None or len(json_string.strip()) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set using a dummy.

        Args:
            **dictionary: Key/value pairs of attributes to set.

        Returns:
            object: An instance of cls with updated attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a JSON file named <Class name>.json.

        Returns:
            list: A list of instantiated objects, or an empty list if file missing.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as f:
                json_str = f.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_str)
        return [cls.create(**d) for d in list_dicts]
