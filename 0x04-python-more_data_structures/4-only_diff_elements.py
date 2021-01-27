#!/usr/bin/python3
def only_diff_elements(set1, set2):
    res = []
    for i, j in set1, set2:
        if i not in set2:
            res.append(i)
        if j not in set1:
            res.append(j)
    return res
