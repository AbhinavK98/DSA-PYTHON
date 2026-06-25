"""LeetCode #26 - Remove Duplicates from Sorted Array.
Question Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        for i, value in enumerate(unique):
            nums[i] = value
        return len(unique)


# Complexity (BruteForce)
#   Time:  O(n log n) — set + sort to collect unique values.
#   Space: O(n)       — set and sorted unique list.


class BetterSolution:
    def solve(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        return write


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — read scans once; write moves only forward.
#   Space: O(1) — in-place overwrite; no extra array.


class OptimalSolution(BetterSolution):
    pass

