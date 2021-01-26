#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []
    else:
        res=[]
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                res[i] = True
            else:
                res[i] = False
    return res
