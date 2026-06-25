"""LeetCode #1480 - Running Sum of 1D Array.
Question Link: https://leetcode.com/problems/running-sum-of-1d-array/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            answer.append(sum(nums[: i + 1]))
        return answer


# Complexity (BruteForce)
#   Time:  O(n^2) — for each i, sum(nums[:i+1]) rescans from start.
#   Space: O(n)   — output list of length n.


class BetterSolution:
    def solve(self, nums: List[int]) -> List[int]:
        return OptimalSolution().solve(nums)


# Complexity (BetterSolution)
#   Time:  O(n) — delegates to single-pass prefix accumulation.
#   Space: O(n) — output array (same as optimal).


class OptimalSolution:
    def solve(self, nums: List[int]) -> List[int]:
        running = 0
        answer: List[int] = []
        for value in nums:
            running += value
            answer.append(running)
        return answer


# Complexity (OptimalSolution)
#   Time:  O(n) — one pass; each running sum updated in O(1).
#   Space: O(n) — answer array (output required by problem).
