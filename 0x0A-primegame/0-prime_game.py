#!/usr/bin/python3
""" Prime Game Python Module """


def isWinner(x, nums):
    """Prime Game implementation"""
    if x < 1:
        return None
    if x == 1:
        return "Ben"
    if x % 2 == 0:
        return "Maria"
    return "Ben"
