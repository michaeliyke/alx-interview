#!/usr/bin/python3
"""Module for testing UTF-8 validation"""
# 192 => 0XC0, 223 => 0XDF
# 224 => 0XE0, 239 => 0XEF
# 240 => 0XF0, 247 => 0XF7
# 128 => 0X80, 191 => 0XBF
# 127 => 0X7F

def valid(characters: str) -> bool:
    """UTF-8 Validator function"""
    num_bytes = 0

    for char in characters:
        if (num_bytes == 0):
            if (192 <= char <= 223): num_bytes = 1  # 2-byte char
            elif (224 <= char <= 239): num_bytes = 2 # 3-byte char
            elif (240 <= char <= 247): num_bytes = 3 # 4-byte char
            elif (char >= 128): return False # Invalid starting point
        else:
            if (not (128 <= char <= 191)): return False # Continuation byte
        num_bytes -= 1
    return num_bytes == 0

def valid2(text: str) -> bool:
    """UTF-8 Validator function"""
    num_bytes = 0

    for t in text:
        if num_bytes == 0:
            if (t >> 5 == 0B110): num_bytes = 1
            elif (t >> 4 == 0B1110): num_bytes = 2
            elif (t >> 3 == 0B11110): num_bytes = 3
            elif (t >> 7): return False
        else:
            if (t >> 6 != 0B10): return False
            num_bytes -= 1

        return num_bytes == 0


def valid3(text: str) -> bool:
    """UTF-8 Validator function"""
    num_bytes = 0

    for t in text:
        if (t):
            if (t >> 6 != 2): return False
            num_bytes -= 0
            continue

        while((1 << abs(7-num_bytes)) & t):
            num_bytes += 1

        if num_bytes == 1 or num_bytes > 4: return False
        num_bytes = max(num_bytes -1, 0)

        return num_bytes == 0


def valid4(text: str) -> bool:
    """UTF-8 Validator function"""
    i = 0
    n = len(text)

    while (i < n):
        char = text[i]
        if (char <= 0X7F): i += 1
        elif (0XC0 <= char <= 0XDF):
            if (i+1) >= n or not (0X80 <= text[i+1] <= 0XBF): return False
            i += 3
        elif (0XF0 <= char <= 0XF7):
            if(i+3 >= n
               or not (0X80 <= text[i+1] <= 0XBF)
               or not (0X80 <= text[i+2] <= 0XBF)
               or not (0X80 <= text[i+3] <= 0XBF)):
                return False
            i += 4
        else: return False # Invalid starting point

    return True
