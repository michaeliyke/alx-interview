#!/usr/bin/python3
"""The minimum operations algorithm in python"""


def minOperations_(n: int) -> int:
    """Implement the minimum operations algorithm in python"""
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return 0


def minOperations(n: int) -> int:
    """Implement the minimum operations algorithm in python"""
    if n <= 1:
        return 0  # Zero operations needed
    i = 2  # 2 is the first prime number
    total = 0  # Total number of operations
    while i <= n:
        # Loop from 2 to n
        if n % i == 0:  # n is divisible by i
            total += i  # Add current prime factor of n (i) to result.
            # Update n by dividing it with the current prime factor(i)
            n = n // i
        else:
            i += 1  # increment i to check the nect potential prime factor
    return total  # total no of operations needed for prime factorizations
