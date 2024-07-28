# 0x04. UTF-8 Validation

A character in UTF-8 can be from 1 to 4 bytes long subject to the following rules:

1. For 1-byte character, the first bit is a 0, followed byt its unicode code
E.g data=[197,130,0]=[11000101,10000010,00000001] Valid
It is a 2-byte charcter followed by a 1-byte character

2. For n-bytes character, the first n bits are all 1s, the n+1 bit is 0,
E.g data=[235,140,4] = [11101011,10000010,00000100] INVALID
The first three bits are 1s, and the fourth bit is 0 means it is a 3-byte character.
The next byte is a continuation byte correctly starting with 10
Essentially, 11101011 - suggests 3-byte character data for starting with 111
10000010 is correct starting with 10, however
00000100 is incorrect starting with 00. It is expected to still start with 10

3. followed by n-1 bytes with most significan 2 bits being 10.

```Python
from typing import List

def validateUTF8(data: List[int]) -> bool:
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


def valid3(chars: List[int]) -> bool:
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


def count_bits(ch: int) -> int:
    bits = 0
    while((1 << abs(7-bits)) & ch):
        bits += 1
    return bits

```
