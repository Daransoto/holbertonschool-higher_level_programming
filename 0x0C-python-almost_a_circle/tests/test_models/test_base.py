#!/usr/bin/python3
"""
Unittest for the class base.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Class for testing.
    """

    def test_give_id(self):
        """ Creating a Base instance with a specific id. """
        b1 = Base(500)
        self.assertEqual(b1.id, 500)
