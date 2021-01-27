#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        items=list(a_dictionary.values)
        items.sort(reverse = True)
        return items[0]
