#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ Function to find a peak on an unsorted list. """
    if not list_of_integers:
        return None

    if len(list_of_integers) <= 3:
        return max(list_of_integers)

    middle = len(list_of_integers) // 2
    if list_of_integers[middle-1] <= list_of_integers[middle]\
       >= list_of_integers[middle+1]:
        return list_of_integers[middle]

    if list_of_integers[middle-1] > list_of_integers[middle]:
        return find_peak(list_of_integers[0:middle-1])

    if list_of_integers[middle] < list_of_integers[middle+1]:
        return find_peak(list_of_integers[middle+1:])
