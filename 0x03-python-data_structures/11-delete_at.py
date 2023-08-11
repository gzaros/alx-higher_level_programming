#!/usr/bin/python3
def delete_at(_list=[], index=0):
    if index < 0 or index > (len(_list) - 1):
        return _list
    _list_2 = _list
    del _list_2[index]
    return _list_2
