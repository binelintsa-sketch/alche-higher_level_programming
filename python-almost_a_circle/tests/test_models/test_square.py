#!/usr/bin/python3
"""
Unittest module for models/square.py
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Tests instantiation of the Square class."""

    def test_inheritance(self):
        """Test if Square inherits from Base and Rectangle."""
        self.assertIsInstance(Square(5), Base)
        self.assertIsInstance(Square(5), Rectangle)

    def test_no_args(self):
        """Test instantiation with no arguments."""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Test instantiation with 1 argument (size)."""
        s1 = Square(5)
        s2 = Square(6)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s2.id, s1.id + 1)

    def test_two_args(self):
        """Test instantiation with 2 arguments (size, x)."""
        s = Square(10, 2)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)

    def test_three_args(self):
        """Test instantiation with 3 arguments (size, x, y)."""
        s = Square(10, 2, 3)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_four_args(self):
        """Test instantiation with 4 arguments (size, x, y, id)."""
        s = Square(10, 2, 3, 99)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 99)


class TestSquareValidation(unittest.TestCase):
    """Tests type and value validation for Square attributes."""

    # Size validations
    def test_size_type_validation(self):
        """Test non-int inputs for size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_size_value_validation(self):
        """Test invalid values for size (<= 0)."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    # X validations
    def test_x_type_validation(self):
        """Test non-int inputs for x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "2")

    def test_x_value_validation(self):
        """Test invalid values for x (< 0)."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)

    # Y validations
    def test_y_type_validation(self):
        """Test non-int inputs for y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, "3")

    def test_y_value_validation(self):
        """Test invalid values for y (< 0)."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 2, -1)


class TestSquareMethods(unittest.TestCase):
    """Tests method implementations in Square."""

    def test_area(self):
        """Test area method inherited from Rectangle."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str_representation(self):
        """Test __str__ method output format."""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_size_getter_setter(self):
        """Test size getter and setter behavior."""
        s = Square(5)
        s.size = 8
        self.assertEqual(s.size, 8)
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)

    def test_to_dictionary(self):
        """Test to_dictionary method output."""
        s = Square(10, 2, 1, 1)
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected)


class TestSquareUpdate(unittest.TestCase):
    """Tests the update method of Square."""

    def test_update_args(self):
        """Test update method with *args."""
        s = Square(5, 0, 0, 1)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(10, 2)
        self.assertEqual(s.size, 2)
        s.update(10, 2, 3)
        self.assertEqual(s.x, 3)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update method with **kwargs."""
        s = Square(5, 0, 0, 1)
        s.update(id=89)
        self.assertEqual(s.id, 89)
        s.update(size=6, x=2)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 2)

    def test_update_args_and_kwargs(self):
        """Test that *args takes precedence over **kwargs."""
        s = Square(5, 0, 0, 1)
        s.update(89, 2, size=10, x=5)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)


if __name__ == "__main__":
    unittest.main()
