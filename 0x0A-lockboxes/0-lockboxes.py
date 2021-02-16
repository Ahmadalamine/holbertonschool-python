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


boxes = [ [7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7], [4, 2, 9, 6, 6, 5, 5], ]
print(canUnlockAll(boxes))