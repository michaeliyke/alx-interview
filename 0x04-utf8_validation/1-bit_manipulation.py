#!/usr/bin/env python3
"""
Main file for testing
"""


def check_LSB(x: int) -> int:
    """Checks if the least significant bit of an integer"""
    return x & 1


def check_LSB_is_1(x: int) -> bool:
    """Checks if the least significant bit of an integer is 1"""
    return (x & 1) == 1


def get_bit_(x: int, index: int) -> int:
    """Get the bit of an integer at an index"""
    # index -= 1
    # mask = 1 << index
    while (index > 1):
        x >>= 1
        index -= 1
    return x & 1


def set_bit_3(x: int, index=3) -> int:
    """Set the nth bit of an integer example 3rd"""
    mask = 1 << (index - 1)
    return x | mask


def get_bit(x: int, index: int):
    """return the bit at index"""
    mask = 1 << (index-1)
    modified = x | mask
    if (modified == x):
        return 1 # bit is 1 so no changes
    else:
        return 0  # bit is 0 and has been set to 1


def unset_bit(x: int, index: int):
    """Set the bit at index to 0 if 1"""
    mask = 1 << (index - 1)
    # Below works below ^ returns 1 if bits are different
    # And since the mask 1 at the index and 0 elsewhere, it works
    return x ^ mask


def toggle_bit_3(x: int, index=3) -> int:
    """Toggle the nth bit of an integer example 3rd"""
    mask = 1 << (index - 1)
    return x ^ mask

def swap_bits2(x: int, p1: int, p2: int) -> int:
    """Swaps bits at positions p1 and p2 in x."""
    # Get the bits at positions p1 and p2
    bit1 = get_bit(x, p1)
    bit2 = get_bit(x, p2)

    # Clear bits at positions p1 and p2
    mask1 = ~(1 << (p1 - 1))
    mask2 = ~(1 << (p2 - 1))
    x &= mask1 & mask2

    # Set bits at positions p1 and p2 based on swapped values
    x |= (bit2 << (p1 - 1)) | (bit1 << (p2 - 1))
    return x

def swap_bits(x: int, indexA: int, indexB: int) -> int:
    """Swap bits at indexes indexA and indexB of an integer"""
    bitA = get_bit(x, indexA)  # bit at indexA
    bitB = get_bit(x, indexB)  # bit at indexB

    if (bitA == 1):
        x=set_bit_3(x, indexB)
    else:
        x=unset_bit(x, indexB)

    if (bitB == 1):
        x=set_bit_3(x, indexA)
    else:
        x=unset_bit(x, indexA)

def count_set_bits(x: int) -> int:
    """Returns the number of set bits in an integer"""
    count = 0
    while x > 0:
        if ((x|1) == x):  # Asks if ORing first bit has any efect on x
            count += 1   # Then the bit is set
        x >>= 1
    return count


if (__name__ == "__main__"):
    n = 11
    print(count_set_bits(n))
    # 3
