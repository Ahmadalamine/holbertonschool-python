#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        s = list(a_dictionary.values())
        s.sort()
        max = s[-1]
        for key, value in a_dictionary.items():
            if value == max:
                return key
