#!/usr/bin/python3
"""doc"""


def canUnlockAll(boxes):
    """d"""

    keys = boxes[0].copy()
    for i in keys:
        try:
            for j in boxes[i]:
                if j not in keys:
                    keys.append(j)
        except IndexError:
            return False
    for i in range(1, len(boxes)):
        if i not in keys:
            return False
    return True
