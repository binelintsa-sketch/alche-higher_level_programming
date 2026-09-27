#!/usr/bin/python3
"""
Unittest for models/rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """TestCase for Rectangle initialization and attribute access."""

    def setUp(self):
        """Reset Base class counter before each test."""
        Base._Base__nb_objects = 0

    def test_basic_instantiation(self):
        """Test creating Rectangle with width and height."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_full_instantiation(self):
        """Test creating Rectangle with all arguments."""
        r = Rectangle(10, 2, 4, 5, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 99)

    def test_getters_setters(self):
        """Test property getters and setters."""
        r = Rectangle(1, 2)
        r.width = 20
        r.height = 30
        r.x = 40
        r.y = 50
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)


if __name__ == '__main__':
    unittest.main()
