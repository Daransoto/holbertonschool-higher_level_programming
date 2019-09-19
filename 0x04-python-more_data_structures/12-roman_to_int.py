#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    length = len(roman_string) - 1
    if roman_string[length] not in conv:
        return 0
    res = conv[roman_string[length]]
    for iterator in range(length, 0, -1):
        if roman_string[iterator] not in conv:
            return 0
        curr = conv[roman_string[iterator]]
        if roman_string[iterator - 1] not in conv:
            return 0
        prev = conv[roman_string[iterator - 1]]
        if iterator > 1:
            if roman_string[iterator - 2] not in conv:
                return 0
            if prev < curr and conv[roman_string[iterator - 2]] <= prev:
                return 0
        res += prev if prev >= curr else -prev
    return res
