#!/usr/bin/python3
"""
Main file for testing
"""

from typing import List

def validateUTF8(chars: List[int]) -> bool:
    """UTF-8 Validator function"""
    # (192-0XC0)(127-0X7F)(223-0XDF)(128-0X80)(191-0XBF)(247-0XF7)(240-0XF0)
    # (224-0XE0)(-0XEF)
    num_bytes = 0

    for ch in chars:
        if num_bytes == 0:
            if (ch >> 5 == 0B110): num_bytes = 1
            elif (ch >> 4 == 0B1110): num_bytes = 2
            elif (ch >> 3 == 0B11110): num_bytes = 3
            elif (ch >> 7): return False
        else:
            if (ch >> 6 != 0B10): return False
            # if (ch >> 6 > 0B10): return False
            num_bytes -= 1

    return num_bytes == 0

validUTF8 = __import__('0-validate_utf8').validUTF8
validUTF8 = validateUTF8


data = [65]
print(validUTF8(data))

data = [197, 130,1]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
