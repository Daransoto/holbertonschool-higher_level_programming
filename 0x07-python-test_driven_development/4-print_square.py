#!/usr/bin/python3
def print_square(size):
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
    if (not size):
        print()
