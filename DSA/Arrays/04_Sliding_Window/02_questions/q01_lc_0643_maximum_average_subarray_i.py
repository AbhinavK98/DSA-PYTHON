"""LeetCode #643 - Maximum Average Subarray I.
Question Link: https://leetcode.com/problems/maximum-average-subarray-i/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int], k: int) -> float:
        best = float('-inf')
        for i in range(len(nums) - k + 1):
            best = max(best, sum(nums[i : i + k]))
        return best / k


# Complexity (BruteForce)
#   Time:  O(n * k) — each window of size k recomputes sum from scratch.
#   Space: O(1)   — only loop indices and best tracker.


class BetterSolution:
    def solve(self, nums: List[int], k: int) -> float:
        return OptimalSolution().solve(nums, k)


# Complexity (BetterSolution)
#   Time:  O(n) — delegates to fixed-size sliding window.
#   Space: O(1) — incremental window sum update.


class OptimalSolution:
    def solve(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        best_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            best_sum = max(best_sum, window_sum)

        return best_sum / k


# Complexity (OptimalSolution)
#   Time:  O(n) — add new right element, drop left in O(1) per step.
#   Space: O(1) — fixed window of size k rolled across array.

