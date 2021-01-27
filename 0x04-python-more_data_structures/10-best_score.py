#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        keyy =''
        max = a_dictionary.values[0]
        for key, value in a_dictionary.items():
            if value > max:
                max = value
                keyy = key
        return keyy
