#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ Function to find a peak on an unsorted list. """
    if not list_of_integers:
        return None
    i = 0
    length = len(list_of_integers) - 1
    while i < length:
        if list_of_integers[i] > list_of_integers[i+1]:
            return list_of_integers[i]
        i += 1
    return list_of_integers[i]
