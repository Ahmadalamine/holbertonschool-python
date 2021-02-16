#!/usr/bin/python3
"""doc"""


def canUnlockAll(boxes):
    """d"""

    c = 0
    keys = boxes[0].copy()
    for i in keys:
        if not boxes[i]:
            c += 1
        for j in boxes[i]:
            if j not in keys:
                keys.append(j)
    res = len(keys) + c
    return len(boxes) == res
