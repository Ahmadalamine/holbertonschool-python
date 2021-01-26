#!/usr/bin/python3
def delete_at(my_list=[], idx):
    if len(my_list) == 0:
        return []
    elif idx < 0 or idx >= len(my_list):
        return my_list
    elif idx == len(my_list) - 1:
        res = my_list[:-1]
    else:
        res = my_list.copy
        j = 0
        for i in range(len(my_list)):
            if i < idx:
                continue
            elif idx == i:
                j = i
                continue
            else:
                res[j] = my_list[i]
                if i == len(my_list) - 1:
                    res = res[:-1]
                j = j+1
        return res
