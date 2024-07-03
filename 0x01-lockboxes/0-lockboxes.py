#!/usr/bin/env python3
"""Module Implementation of Lockboxes algorithm using BFS"""
from collections import deque
from typing import List


def canUnlockAll(boxes: List[List[int]]):
    """Implementation of Lockboxes algorithm using BFS"""
    unprocessed = deque([0])  # Queue of unprocessed indexes, begin with 0th
    processed = set([0])  # Record of already processed indexes, begin with 0th

    while unprocessed:
        current_box_index = unprocessed.popleft()
        current_box = boxes[current_box_index]

        # Iterate the keys of box and queue respective boxes for processing
        for key in current_box:
            # if boxes[key] exists, and has not been processed yet, enqueue it
            if key >= 0 and key < len(boxes) and key not in processed:
                processed.add(key)  # Mark it as unlocked(visited)
                unprocessed.append(key)  # Enque box for processing
    # After the BFS traversal completes, check if the number of visited boxes
    # is equal to the number of boxes
    # If yes, return true (all boxes were visted - opened)
    # else return false (some boxes were not visited - locked)
    return True if len(boxes) == len(processed) else False
