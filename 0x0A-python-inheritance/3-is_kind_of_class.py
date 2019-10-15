#!/usr/bin/python3
"""
This module contains the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if the object is an instance of, or if the obj
    is an instance of a class that inherited from, the specified class.
    Otherwise returns False.
    """
    return isinstance(obj, a_class)
