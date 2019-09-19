#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return
    conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    length = len(roman_string) - 1
    res = conv[roman_string[length]]
    for iterator in range(length, 0, -1):
        curr = conv[roman_string[iterator]]
        prev = conv[roman_string[iterator - 1]]
        res += prev if prev >= curr else -prev
    return res
