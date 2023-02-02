#!/usr/bin/python3
"""Script will determine if list of lists can be unlocked"""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
