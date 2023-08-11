#!/usr/bin/python3
def replace_in_list(_list, index, elem):
    if index < 0:
        return _list
    elif index > len(_list) - 1:
        return _list
    else:
        _list[index] = elem
        return _list
