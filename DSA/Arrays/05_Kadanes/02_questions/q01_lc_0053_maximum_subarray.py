"""LeetCode #53 - Maximum Subarray.
Question Link: https://leetcode.com/problems/maximum-subarray/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> int:
        best = nums[0]
        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current += nums[j]
                best = max(best, current)
        return best


# Complexity (BruteForce)
#   Time:  O(n^2) — try every subarray start i and end j.
#   Space: O(1)   — only running subarray sum and best tracker.


class BetterSolution:
    def solve(self, nums: List[int]) -> int:
        return OptimalSolution().solve(nums)


# Complexity (BetterSolution)
#   Time:  O(n) — delegates to Kadane's single pass.
#   Space: O(1) — only two running variables.


class OptimalSolution:
    def solve(self, nums: List[int]) -> int:
        # Kadane's: max subarray ending here.
        best_ending_here = nums[0]
        best_so_far = nums[0]

        for i in range(1, len(nums)):
            best_ending_here = max(nums[i], best_ending_here + nums[i])
            best_so_far = max(best_so_far, best_ending_here)

        return best_so_far


# Complexity (OptimalSolution)
#   Time:  O(n) — one pass; extend-or-restart decision per element.
#   Space: O(1) — best_ending_here and best_so_far only.

