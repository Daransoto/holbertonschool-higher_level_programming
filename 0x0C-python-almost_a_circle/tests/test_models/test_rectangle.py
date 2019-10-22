#!/usr/bin/python3
"""
Unittest for the class base.
"""
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    Class for testing.
    """

    def test_empty(self):
        """ Test for an empty instantiation. """
        with self.assertRaises(TypeError):
            s1 = Rectangle()
