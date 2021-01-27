#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        newlist = set(my_list)
        res=0
        for i in newlist:
            res = res + i
    else:
        return None
    return res
