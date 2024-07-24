#!/usr/bin/python3
"""Module for testing UTF-8 validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    """num_bytes = 0

    for num in data:
        mask = 1 << 7
        if not num_bytes:
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            if not num_bytes:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if num >> 6 != 2:
                return False
        num_bytes -= 1

    return num_bytes == 0
    """
    """bytes = 0
    for byte in data:
        if bytes:
            if byte >> 6 != 2:
                return False
            bytes -= 1
            continue
        while (1 << abs(7 - bytes)) & byte:
            bytes += 1
        if bytes == 1 or bytes > 4:
            return False
        bytes = max(bytes - 1, 0)
    return bytes == 0
    """
    pass
