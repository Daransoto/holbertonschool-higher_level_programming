#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for elem in row:
            count += 1
            print('{}'.format(elem), end=(" " if count < len(row) else ""))
        print()
