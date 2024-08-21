#!/usr/bin/python3
"""Module for the coin change making algorithm"""


def makeChange(coins, total):
    """Coin change making algorithm"""
    if total <= 0:
        return 0

    # A List to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value to update the minimum number of
    # coins needed for each total value
    for coin in coins:
        # Updating takes place here
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If infinite still, then the total can't be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]
