"""
1. Best Time to Buy and Sell Stock
Easy
Given an array prices where prices[i] is the price of a given stock on day i, return the maximum profit you can achieve from one transaction.

You may only complete one transaction (buy one and sell one share of the stock).

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 and sell on day 5, profit = 6-1 = 5.
Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No transaction is done, profit = 0.
"""

from typing import List


def solution1_bruteforce(prices: List[int]) -> int:
    # Step 1: Set best profit to 0.
    # Step 2: For each day i as the buy day, consider every later day j as the sell day.
    # Step 3: Compute profit = prices[j] - prices[i] and keep the maximum profit seen.
    # Step 4: After all buy/sell pairs are checked, return the best profit.
    # Time Complexity: O(n^2) because the nested loops consider every pair of buy and sell days.
    # Space Complexity: O(1) because only a few scalar variables are maintained.
    n = len(prices)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, prices[j] - prices[i])
    return best


def solution2_average(prices: List[int]) -> int:
    # Step 1: Initialize min_price to infinity and best profit to 0.
    # Step 2: Iterate through prices once from left to right.
    # Step 3: Update min_price when a lower stock price is found.
    # Step 4: Compute today_profit = current price - min_price and update best profit if it is larger.
    # Step 5: Return best profit after scanning all days.
    # Time Complexity: O(n) because the algorithm makes a single pass over the price list.
    # Space Complexity: O(1) because it only uses a couple of scalar variables regardless of input size.
    min_price = float('inf')
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best


def solution3_optimal(prices: List[int]) -> int:
    # Step 1: Keep track of the smallest price seen so far and the maximum profit.
    # Step 2: For each price, if it is smaller than the smallest seen, update the smallest.
    # Step 3: Otherwise calculate profit if sold today and update maximum profit if larger.
    # Step 4: Repeat until all days are processed and return the maximum profit.
    # Time Complexity: O(n) because each price is processed exactly once with constant work per price.
    # Space Complexity: O(1) because no additional data structures proportional to the input size are used.
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit


# Pattern: Greedy one-pass, track the minimum price and update maximum profit.


if __name__ == "__main__":
    assert solution3_optimal([7,1,5,3,6,4]) == 5
    assert solution3_optimal([7,6,4,3,1]) == 0
    assert solution3_optimal([1,2,3,4,5]) == 4
    print("best_time_to_buy_and_sell_stock: all tests passed")
