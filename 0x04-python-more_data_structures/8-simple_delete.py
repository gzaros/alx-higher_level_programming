#!/usr/bin/python3
def simple_delete(a_dictionary, val=""):
    if val in a_dictionary.keys():
        del a_dictionary[val]
        return a_dictionary
    else:
        return a_dictionary
