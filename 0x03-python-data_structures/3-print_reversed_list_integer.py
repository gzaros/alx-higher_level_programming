#!/usr/bin/python3
def print_reversed_list_integer(_list=[]):
    """ display all integers from list, in reverse order."""
    if not _list:
        pass
    else:
        _list.reverse()
        for item in _list:
            print('{:d}'.format(item))
