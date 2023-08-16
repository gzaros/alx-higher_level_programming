#!/usr/bin/python3
def update_dictionary(a_dictionary, val, value):
    if val in a_dictionary.keys():
        a_dictionary[val] = value
    else:
        a_dictionary[val] = value
    return a_dictionary
