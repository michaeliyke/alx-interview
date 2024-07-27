#!/usr/bin/python3
"""Module for testing UTF-8 validation"""
# (192-0XC0)(127-0X7F)(223-0XDF)(128-0X80)(191-0XBF)(247-0XF7)(240-0XF0)
# (224-0XE0)(-0XEF)
# RANGES
# (U+0000-U+007F)(0x0000-0x007F)(0000 0000 - 0111 1111)(0-127)
# (U+0080-U+07FF)(0x0080-0x07FF)(0000 1000 0000 - 0111 1111 1111)(128-2,047)
# (U+0800-U+FFFF)(0x0800-0xFFFF)(0000 1000 0000 0000-1111 1111 1111 1111)--
# --(2,048-65,535)
# (U+10000-U+10FFFF)( 0x10000-0x10FFFF)--
# --(0001 0000 0000 0000 0000-0001 0000 1111 1111 1111 1111)--
# --(65,536-1,114,111)

def valid(chars: str) -> bool:
    """UTF-8 Validator function"""
    num_bytes = 0

    for ch in chars:
        if (num_bytes == 0):
            if (192 <= ch <= 223): num_bytes = 1  # 2-byte char
            elif (224 <= ch <= 239): num_bytes = 2 # 3-byte char
            elif (240 <= ch <= 247): num_bytes = 3 # 4-byte char
            elif (ch >= 128): return False # Invalid starting point
        else:
            if (not (128 <= ch <= 191)): return False # Continuation byte
        num_bytes -= 1
    return num_bytes == 0

def valid2(chars: str) -> bool:
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
            num_bytes -= 1

        return num_bytes == 0


def valid3(chars: str) -> bool:
    """UTF-8 Validator function"""
    num_bytes = 0

    for ch in chars:
        if (ch):
            if (ch >> 6 != 2): return False
            num_bytes -= 0
            continue

        while((1 << abs(7-num_bytes)) & ch):
            num_bytes += 1

        if num_bytes == 1 or num_bytes > 4: return False
        num_bytes = max(num_bytes -1, 0)

        return num_bytes == 0


def valid4(chars: str) -> bool:
    """UTF-8 Validator function"""
    i = 0
    n = len(chars)
    # (192-0XC0)(127-0X7F)(223-0XDF)(128-0X80)(191-0XBF)(247-0XF7)(240-0XF0)
    # (224-0XE0)(-0XEF)
    while (i < n):
        ch = chars[i]
        if (ch <= 0X7F): i += 1
        elif (192 <= ch <= 223):
            if (i+1) >= n or not (128 <= chars[i+1] <= 191): return False
            i += 3
        elif (0XF0 <= ch <= 247):
            if(i+3 >= n
               or not (128 <= chars[i+1] <= 191)
               or not (128 <= chars[i+2] <= 191)
               or not (128 <= chars[i+3] <= 191)): return False
            i += 4
        else: return False # Invalid starting point

    return True

def validV(chars: str) -> bool:
    """UTF-8 Validator function"""
    # (192-0XC0)(127-0X7F)(223-0XDF)(128-0X80)(191-0XBF)(247-0XF7)(240-0XF0)
    # (224-0XE0)(-0XEF)
    num_bytes = 0

    for ch in chars:
        if (num_bytes == 0):
            if (192 <= ch <= 223): num_bytes = 1  # 2-byte char
            elif (224 <= ch <= 239): num_bytes = 2 # 3-byte char
            elif (240 <= ch <= 247): num_bytes = 3 # 4-byte char
            elif (ch >= 128): return False # Invalid starting point
        else:
            if (not (128 <= ch <= 191)): return False # Continuation byte
        num_bytes -= 1
    return num_bytes == 0
