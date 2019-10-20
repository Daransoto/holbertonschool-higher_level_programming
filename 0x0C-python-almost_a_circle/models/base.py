#!/usr/bin/python3
"""
This module contains the class Base.
"""
import json


class Base:
    """
    Base class for the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of the class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Json representation of a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
