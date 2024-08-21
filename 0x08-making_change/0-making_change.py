#!/usr/bin/python3
"""Module for the coin change making algorithm"""


def makeChange(coins, total):
    """Calculate the minimum number of coins needed to make a given total"""
    if total <= 0:
        return 0

    # A List to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin
    for coin in coins:
        # Update the dp array for each value from coin to total
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity
    # it means it's not possible to make that amount with the given coins
    if dp[total] == float('inf'):
        return -1

    return dp[total]
