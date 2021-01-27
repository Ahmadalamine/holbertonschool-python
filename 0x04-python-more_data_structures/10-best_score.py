#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        items = a_dictionary.values()
        items.sort()
        return items[-1]
