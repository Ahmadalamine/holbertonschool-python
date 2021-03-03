#!/usr/bin/python3
"""doc"""


def validUTF8(data):
    """doc"""
    expected_length = 0
    for i in data:
        if i & 256 == 0:
            expected_length = 1
        elif i & 192 == 192:
            expected_length = 2
        elif i & 224 == 224:
            expected_length = 3
        elif i & 240 == 240:
            expected_length = 4
        else:
            return False
    expected_length -= 1
    while expected_length > 0:
        i += 1
        if i >= len(data):
            return False
        if bin(data[i]) & 0b11000000 != 0b10000000:
            return False
        expected_length -= 1
    return True
