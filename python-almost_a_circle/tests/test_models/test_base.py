#!/usr/bin/python3
"""
Unittest for models/base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestCase class for the Base class."""

    def setUp(self):
        """Reset private __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id_assignment(self):
        """Test auto-incrementing id assignment when id is None."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id_assignment(self):
        """Test passing an explicit id value."""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_mixed_id_assignment(self):
        """Test mixing auto-incrementing and explicit id assignments."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_negative_id(self):
        """Test passing a negative integer for id."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_zero_id(self):
        """Test passing zero for id."""
        b = Base(0)
        self.assertEqual(b.id, 0)


if __name__ == '__main__':
    unittest.main()
