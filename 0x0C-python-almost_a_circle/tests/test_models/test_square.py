#!/usr/bin/python3
"""
Unittest for the class square.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Class for testing.
    """

    def test_empty(self):
        """ Test for an empty instantiation. """
        with self.assertRaises(TypeError):
            s1 = Square()
