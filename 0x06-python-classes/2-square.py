#!/usr/bin/bash
class Square:
    __size = 0
    def __init__(self, size=0):
        try:
            __size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
