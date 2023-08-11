#!/usr/bin/python3
"""Code to Display Numbers in a List"""


def print_list_integer(my_list=[]):
    """Display all integers of a list"""
    for n in my_list:
        print("{:d}".format(n))
