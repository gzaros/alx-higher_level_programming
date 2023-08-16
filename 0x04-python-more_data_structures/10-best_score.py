#!/usr/bin/python3
def best_score(dic):
    """find the max of a dictionary"""
    if not dic:
        return None
    return max(dic, key=dic.get())
