"""LeetCode #121 - Best Time to Buy and Sell Stock.
Question Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


class BruteForce:
    def solve(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                best = max(best, prices[j] - prices[i])
        return best


# Complexity (BruteForce)
#   Time:  O(n^2) — every buy day i paired with every later sell day j.
#   Space: O(1)   — only best profit tracker.


class BetterSolution:
    def solve(self, prices: List[int]) -> int:
        return OptimalSolution().solve(prices)


# Complexity (BetterSolution)
#   Time:  O(n) — delegates to min-price-so-far greedy pass.
#   Space: O(1) — only min_price and best_profit.


class OptimalSolution:
    def solve(self, prices: List[int]) -> int:
        min_price = float('inf')
        best_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            best_profit = max(best_profit, price - min_price)
        return best_profit


# Complexity (OptimalSolution)
#   Time:  O(n) — one pass; update min buy and max profit seen.
#   Space: O(1) — greedy: best sell always follows cheapest prior buy.

