#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return (0, 0)
    elif len(tuple_a) == 0:
        sum1 = tuple_b[0]
        sum2 = tuple_b[1]
    elif len(tuple_b) == 0:
        sum1 = tuple_a[0]
        sum2 = tuple_a[1]
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
