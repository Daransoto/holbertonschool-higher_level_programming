#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new = a_dictionary.copy()
        for key in a_dictionary:
            new[key] = a_dictionary[key] * 2
        return new
    else:
        return
