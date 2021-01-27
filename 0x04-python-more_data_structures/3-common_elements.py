#!/usr/bin/python3
def common_elements(set1, set2):
    res = []
    for i in set1:
        if i in set2:
            res.append(i)
    return res

