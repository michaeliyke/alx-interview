#!/usr/bin/python3
"""Module for the coin change making algorithm"""


def makeChange(coins, total):
    """Coin change making algorithm"""
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed for each total value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the minimum number of coins needed for each total value
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the minimum number of coins needed for the total value is still infinity, it means the total cannot be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]
