"""
Question: Contains Duplicate
LeetCode: #217
Question Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Pattern: HashMap/HashSet lookup
"""

from typing import List, Set


class BruteForce:
    def solve(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# Complexity (BruteForce)
#   Time:  O(n^2) — compares every pair (i, j) for equality.
#   Space: O(1)   — no auxiliary storage beyond loop indices.


class BetterSolution:
    def solve(self, nums: List[int]) -> bool:
        # Sorting makes equal values adjacent.
        sorted_nums = sorted(nums)
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                return True
        return False


# Complexity (BetterSolution)
#   Time:  O(n log n) — sorting costs O(n log n); one linear scan for neighbors.
#   Space: O(n)       — sorted copy of the array.


class OptimalSolution:
    def solve(self, nums: List[int]) -> bool:
        seen: Set[int] = set()
        for value in nums:
            if value in seen:
                return True
            seen.add(value)
        return False


# Complexity (OptimalSolution)
#   Time:  O(n) — one pass; set membership check is O(1) average.
#   Space: O(n) — set holds up to n distinct values in worst case.


if __name__ == '__main__':
    print(OptimalSolution().solve([1, 2, 3, 1]))

