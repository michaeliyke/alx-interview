#!/usr/bin/python3
"""Module for the coin change making algorithm"""

from collections import deque


def makeChange0(coins, total):
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


def makeChange(coins, total):
    """Calculate the minimum number of coins required to make up a given total
    using the BFS (Breath First Search) approach."""
    if total <= 0:
        return 0

    # Queue to perform BFS, starting from the total value of 0 with 0 coins used
    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        current_total, coin_count = queue.popleft()
        # Explore the next states by adding each coin

        for coin in coins:
            new_total = current_total + coin

            # If the new total equals the target total, return the count
            if new_total == total:
                return coin_count+1

            # If the new total ie less than the target and not yet visited,
            # add it to the queue
            if new_total < total and new_total not in visited:
                visited.add(new_total)
                queue.append((new_total, coin_count+1))

    # If no combination of coins can sum to the total, return -1
    return -1
