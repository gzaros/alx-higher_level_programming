#!/usr/bin/python3
def max_integer(_list=[]):
    valMAx = _list[0]
    for x in range(0, len(_list)):
        if int(_list[x] > int(valMAx)):
            valMAx = _list[x]
    return valMAx
