"""LeetCode #31 - Next Permutation.
Question Link: https://leetcode.com/problems/next-permutation/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> None:
        # Brute force by generating all permutations is not practical here.
        # Keep as conceptual placeholder for interview discussion.
        OptimalSolution().solve(nums)


# Complexity (BruteForce)
#   Time:  O(n!) — generating all permutations (conceptual placeholder).
#   Space: O(n)   — recursion/stack for permutation generation.


class BetterSolution:
    def solve(self, nums: List[int]) -> None:
        OptimalSolution().solve(nums)


# Complexity (BetterSolution)
#   Time:  O(n) — same as optimal (delegates).
#   Space: O(1) — in-place swaps only.


class OptimalSolution:
    def solve(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# Complexity (OptimalSolution)
#   Time:  O(n) — find pivot + swap + reverse suffix each linear.
#   Space: O(1) — in-place: pivot, swap successor, reverse tail.

