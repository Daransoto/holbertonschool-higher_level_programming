#!/usr/bin/python3
def text_indentation(text):
    newline = 0
    spaces = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char == ' ':
            spaces += 1
        elif char == '.' or char == '?' or char == ':':
            print(char + "\n")
            newline = 1
        elif not newline:
            print(" " * spaces + char, end="")
            spaces = 0
        else:
            print(char, end="")
            newline = 0
            spaces = 0
