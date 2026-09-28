#!/usr/bin/python3
"""
Unittest module for models/base.py
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Tests instantiation and ID assignment of the Base class."""

    def setUp(self):
        """Reset private instance count before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id_increment(self):
        """Test automatic ID increment when id is None."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test explicit ID assignment."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_custom_id_does_not_increment_nb_objects(self):
        """Test that explicit ID does not increment internal counter."""
        b1 = Base()
        b2 = Base(89)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 89)
        self.assertEqual(b3.id, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Tests to_json_string static method."""

    def test_to_json_string_none(self):
        """Test None argument returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test empty list returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test valid list of dictionaries returns JSON string."""
        dicts = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        json_str = Base.to_json_string(dicts)
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, '[{"id": 1, "width": 10, '
                                   '"height": 7, "x": 2, "y": 8}]')


class TestBaseFromJsonString(unittest.TestCase):
    """Tests from_json_string static method."""

    def test_from_json_string_none(self):
        """Test None argument returns empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        """Test empty string returns empty list."""
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("   "), [])

    def test_from_json_string_valid(self):
        """Test valid JSON string returns list of dictionaries."""
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        result = Base.from_json_string(json_str)
        expected = [{'id': 89, 'width': 10, 'height': 4}]
        self.assertEqual(result, expected)


class TestBaseSaveToFile(unittest.TestCase):
    """Tests save_to_file class method."""

    def tearDown(self):
        """Clean up generated JSON files after tests."""
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_none(self):
        """Test save_to_file with None writes empty list JSON."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with empty list writes empty list JSON."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rectangles(self):
        """Test saving list of Rectangle objects."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        expected = Base.to_json_string([r1.to_dictionary(),
                                        r2.to_dictionary()])
        self.assertEqual(content, expected)


class TestBaseCreate(unittest.TestCase):
    """Tests create class method."""

    def test_create_rectangle(self):
        """Test creating a Rectangle instance from dictionary."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test creating a Square instance from dictionary."""
        s1 = Square(5, 1, 2, 9)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests load_from_file class method."""

    def tearDown(self):
        """Clean up generated JSON files after tests."""
        for filename in ["Rectangle.json", "Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_load_from_file_file_not_found(self):
        """Test load_from_file when file does not exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        """Test load_from_file loading saved Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertEqual(len(output), 2)
        self.assertEqual(str(output[0]), str(r1))
        self.assertEqual(str(output[1]), str(r2))

    def test_load_from_file_square(self):
        """Test load_from_file loading saved Square instances."""
        s1 = Square(5, 1, 3, 10)
        s2 = Square(9, 0, 0, 11)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertEqual(len(output), 2)
        self.assertEqual(str(output[0]), str(s1))
        self.assertEqual(str(output[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
