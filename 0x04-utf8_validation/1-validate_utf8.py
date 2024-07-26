#!/usr/bin/python3
"""Module for testing UTF-8 validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            # 0b110xxxxx (192 = 0b11000000, 223 = 0b11011111)
            if 192 <= num <= 223:  # 2-byte character
                num_bytes = 1
            # 0b1110xxxx (224 = 0b11100000, 239 = 0b11101111)
            elif 224 <= num <= 239:  # 3-byte character
                num_bytes = 2
            # 0b11110xxx (240 = 0b11110000, 247 = 0b11110111)
            elif 240 <= num <= 247:  # 4-byte character
                num_bytes = 3
            # 0b10xxxxxx or invalid (128 = 0b10000000)
            elif num >= 128:  # Invalid starting byte
                return False
        else:
            # 0b10xxxxxx (128 = 0b10000000, 191 = 0b10111111)
            if not (128 <= num <= 191):  # Continuation byte
                return False
            num_bytes -= 1

    return num_bytes == 0


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    bytes_to_process = 0

    for byte in data:
        if bytes_to_process == 0:
            if byte >> 5 == 0b110:
                bytes_to_process = 1
            elif byte >> 4 == 0b1110:
                bytes_to_process = 2
            elif byte >> 3 == 0b11110:
                bytes_to_process = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_to_process -= 1

    return bytes_to_process == 0


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    bytes = 0
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


def is_valid_utf8(data):
    """Checks if the given byte string is valid UTF-8."""
    i = 0
    n = len(data)

    while i < n:
        byte = data[i]

        if byte <= 0x7F:
            # 1-byte character (ASCII)
            i += 1
        elif 0xC0 <= byte <= 0xDF:
            # 2-byte character
            if i + 1 >= n or not (0x80 <= data[i + 1] <= 0xBF):
                return False
            i += 2
        elif 0xE0 <= byte <= 0xEF:
            # 3-byte character
            if i + 2 >= n or not (0x80 <= data[i + 1] <= 0xBF) or not (0x80 <= data[i + 2] <= 0xBF):
                return False
            i += 3
        elif 0xF0 <= byte <= 0xF7:
            # 4-byte character
            if i + 3 >= n or not (0x80 <= data[i + 1] <= 0xBF) or not (0x80 <= data[i + 2] <= 0xBF) or not (0x80 <= data[i + 3] <= 0xBF):
                return False
            i += 4
        else:
            # Invalid starting byte
            return False

    return True
