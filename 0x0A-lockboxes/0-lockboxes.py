#!/usr/bin/python3
"""doc"""


def canUnlockAll(boxes):
    """d"""

    keys = boxes[0].copy()
    for i in keys:
        for j in boxes[i]:
            if j not in keys:
                keys.append(j)
    for i in range(len(boxes)):
        if i not in keys:
            return False
    return True
