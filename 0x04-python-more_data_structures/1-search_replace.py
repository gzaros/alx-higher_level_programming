#!/usr/bin/python3
def search_replace(_list, search, replace):
    return ([element if element != search else replace for element in _list])
