#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test list with a single element."""
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_floats(self):
        """Test list of floats."""
        floats = [1.54, 6.34, -9.124, 15.4, 6.0]
        self.assertEqual(max_integer(floats), 15.4)

    def test_ints_and_floats(self):
        """Test list of ints and floats."""
        ints_and_floats = [1.54, 15.4, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.4)

    def test_string(self):
        """Test a string."""
        string = "rrreally"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Hello", "its", "me", "Noone"]
        self.assertEqual(max_integer(strings), "Noone")

    def test_empty_string(self):
        """Test empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
