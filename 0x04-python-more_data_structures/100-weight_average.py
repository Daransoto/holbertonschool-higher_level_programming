#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = sum([v * w for v, w in my_list])
    den = sum([w for v, w in my_list])
    if not den:
        return 0
    return num/den
