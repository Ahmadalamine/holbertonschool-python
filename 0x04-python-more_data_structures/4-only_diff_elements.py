#!/usr/bin/python3
def only_diff_elements(set1, set2):
    res = []
    for i in set1:
        if i not in set2:
            res.append(i)
    for i in set2:
        if i not in set1:
            res.append(i)
    return res
