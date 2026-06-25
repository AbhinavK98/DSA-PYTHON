"""LeetCode #169 - Majority Element.
Question Link: https://leetcode.com/problems/majority-element/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> int:
        for value in nums:
            if nums.count(value) > len(nums) // 2:
                return value
        return -1


# Complexity (BruteForce)
#   Time:  O(n^2) — for each value, nums.count scans entire array.
#   Space: O(1)   — no extra structures.


class BetterSolution:
    def solve(self, nums: List[int]) -> int:
        freq = {}
        for value in nums:
            freq[value] = freq.get(value, 0) + 1
            if freq[value] > len(nums) // 2:
                return value
        return -1


# Complexity (BetterSolution)
#   Time:  O(n) — single pass with hash map frequency updates.
#   Space: O(n) — map stores counts for distinct elements.


class OptimalSolution:
    def solve(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for value in nums:
            if count == 0:
                candidate = value
            count += 1 if value == candidate else -1
        return candidate


# Complexity (OptimalSolution)
#   Time:  O(n) — Boyer-Moore vote canceling in one pass.
#   Space: O(1) — only candidate and count (majority guaranteed).

