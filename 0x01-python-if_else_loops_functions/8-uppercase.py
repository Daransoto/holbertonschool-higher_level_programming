#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 123:
            print("{}".format(str[i] if ord(str[i]) <= 97 or
                    ord(str[i]) >= 123 else chr(ord(str[i]) - 32)), end="")
    print()
