#!/usr/bin/python3
def print_matrix_integer(_mtx=[[]]):
    """Display a matrix of integers"""
    for i in range(0, len(_mtx)):
        for j in range(0, len(_mtx[i])):
            if not j == 0:
                print(" ", end='')
            print("{:d}".format(_mtx[i][j]), end='')
        print()
