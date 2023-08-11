#!/usr/bin/python3
def multiple_returns(sst):
    "Reterive the length of a tuple and the first element"
    if not sst:
        return (0, None)
    return (len(tuple(sst)), tuple(sst)[0])
