#!/usr/bin/python3
def square_matrix_simple(mtx=[]):
    if not mtx:
        return None

    return list(list(map(lambda n: n*n, row)) for row in mtx)
