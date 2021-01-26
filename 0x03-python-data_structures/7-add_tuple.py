#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None:
        return tuple_b
    elif tuple_b is None:
        return tuple_a
    elif len(tuple_a) == 1:
        sum1 = tuple_a[0] + tuple_b[0]
        sum2 = tuple_b[1]
    elif len(tuple_b) == 1:
        sum1 = tuple_a[0] + tuple_b[0]
        sum2 = tuple_a
    else:
        sum1 = tuple_a[0] + tuple_b[0]
        sum2 = tuple_a[1] + tuple_b[1]
    res = (sum1, sum2)
    return res
