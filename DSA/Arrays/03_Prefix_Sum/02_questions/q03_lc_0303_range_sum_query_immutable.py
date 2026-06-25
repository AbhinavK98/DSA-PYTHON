"""LeetCode #303 - Range Sum Query Immutable.
Question Link: https://leetcode.com/problems/range-sum-query-immutable/
"""
from typing import List


class BruteForceNumArray:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left : right + 1])


# Complexity (BruteForceNumArray)
#   Time:  O(n) per query — sum slices left..right each call.
#   Space: O(1) extra — stores only reference to input array.


class BetterNumArray:
    def __init__(self, nums: List[int]) -> None:
        self.prefix = [0]
        for value in nums:
            self.prefix.append(self.prefix[-1] + value)

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Complexity (BetterNumArray / OptimalNumArray)
#   Time:  O(n) preprocess + O(1) per query — prefix diff is constant.
#   Space: O(n) — prefix array of length n + 1.


class OptimalNumArray(BetterNumArray):
    pass

