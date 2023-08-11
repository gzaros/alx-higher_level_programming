#!/usr/bin/python3
def element_at(_list, index):
    if index < 0:
        return None
    elif index > len(_list):
        return None
    else:
        return _list[index]
