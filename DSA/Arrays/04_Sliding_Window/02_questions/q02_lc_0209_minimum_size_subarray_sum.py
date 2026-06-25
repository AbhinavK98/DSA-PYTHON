"""LeetCode #209 - Minimum Size Subarray Sum.
Question Link: https://leetcode.com/problems/minimum-size-subarray-sum/
"""
from typing import List


class BruteForce:
    def solve(self, target: int, nums: List[int]) -> int:
        answer = float('inf')
        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current += nums[j]
                if current >= target:
                    answer = min(answer, j - i + 1)
                    break
        return 0 if answer == float('inf') else int(answer)


# Complexity (BruteForce)
#   Time:  O(n^2) worst — every start i, extend j until sum >= target.
#   Space: O(1)   — only running sum and answer tracker.


class BetterSolution:
    def solve(self, target: int, nums: List[int]) -> int:
        return OptimalSolution().solve(target, nums)


# Complexity (BetterSolution)
#   Time:  O(n) — delegates to variable sliding window.
#   Space: O(1) — only window pointers and sum.


class OptimalSolution:
    def solve(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        best = float('inf')

        for right, value in enumerate(nums):
            window_sum += value
            while window_sum >= target:
                best = min(best, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if best == float('inf') else int(best)


# Complexity (OptimalSolution)
#   Time:  O(n) — right expands once; left shrinks at most n times total.
#   Space: O(1) — window sum tracked with two indices.

