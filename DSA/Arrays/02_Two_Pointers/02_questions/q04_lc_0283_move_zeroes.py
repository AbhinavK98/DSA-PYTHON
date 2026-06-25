"""LeetCode #283 - Move Zeroes.
Question Link: https://leetcode.com/problems/move-zeroes/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> None:
        non_zero = [x for x in nums if x != 0]
        zero_count = len(nums) - len(non_zero)
        nums[:] = non_zero + [0] * zero_count


# Complexity (BruteForce)
#   Time:  O(n) — filter pass + rebuild array.
#   Space: O(n) — `non_zero` list and zero padding.


class BetterSolution:
    def solve(self, nums: List[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — read visits each index once; swaps are O(1).
#   Space: O(1) — in-place swap; no extra array.


class OptimalSolution(BetterSolution):
    pass

