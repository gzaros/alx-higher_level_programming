#!/usr/bin/python3
def new_in_list(_list, index, element):
    """Retreive new list _list_2 item at position index set to elelement"""
    if index < 0 or index > (len(_list) - 1):
        return _list
    _list_2 = [item for item in _list]
    _list_2[index] = element
    return _list_2
