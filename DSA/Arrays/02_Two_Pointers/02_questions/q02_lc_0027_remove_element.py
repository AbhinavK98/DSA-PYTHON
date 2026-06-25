"""LeetCode #27 - Remove Element.
Question Link: https://leetcode.com/problems/remove-element/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int], val: int) -> int:
        kept = [x for x in nums if x != val]
        nums[: len(kept)] = kept
        return len(kept)


# Complexity (BruteForce)
#   Time:  O(n) — list comprehension scans all elements once.
#   Space: O(n) — new list `kept` stores up to n elements.


class BetterSolution:
    def solve(self, nums: List[int], val: int) -> int:
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — single read pointer; each element visited once.
#   Space: O(1) — in-place compaction without auxiliary list.


class OptimalSolution(BetterSolution):
    pass

