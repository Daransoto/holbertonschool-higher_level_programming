#!/usr/bin/python3
"""Rectangle.

This module contains the definition of a rectangle..

"""


class Rectangle:
    """Class that defines a rectangle with its width and height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """The __init__ method uses a defaul width and height of 0.

        Args:
            width: Width for the rectangle.
            height: Height for the rectangle.
        Attributes:
            width: Width of the rectangle.
            height: Height of the rectangle.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that calculates the area of a rectangle.

        Returns (int): The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Function that calculates the perimeter of a rectangle.

        Returns (int): The perimeter of the rectangle
                       (0 if one of its sides is 0).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        my_str = ("#" * self.__width + "\n") * self.__height
        return my_str[:-1]

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height)\
                + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
