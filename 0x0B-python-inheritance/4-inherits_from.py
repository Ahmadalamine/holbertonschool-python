#!/usr/bin/python3
"""doc"""


def inherits_from(obj, a_class):
    """doc"""
    if issubclass(type(obj), a_class) and not isinstance(obj, type(a_class)):
        return True
    return False
