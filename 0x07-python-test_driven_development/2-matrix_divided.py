#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
    length = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix\
                            (list of lists) of integers/floats")
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("matrix must be a matrix\
                                (list of lists) of integers/floats")
        length.append(len(row))
    if not len(set(length)) <= 1:
        raise TypeError("Each row of the matrix must have the same size")
    new = []
    temp = []
    for row in matrix:
        for elem in row:
            temp.append(round(elem / div, 2))
        new.append(temp.copy())
        temp.clear()
    return new
