#!/usr/bin/python3
def no_c(_string):
    _string_2 = "".join([char for char in _string if char.upper() != "C"])
    return (_string_2)
print(no_c("No further C. Come and Code along with me"))
