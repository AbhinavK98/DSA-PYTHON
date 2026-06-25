"""LeetCode #11 - Container With Most Water.
Question Link: https://leetcode.com/problems/container-with-most-water/
"""
from typing import List


class BruteForce:
    def solve(self, height: List[int]) -> int:
        best = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                best = max(best, area)
        return best


# Complexity (BruteForce)
#   Time:  O(n^2) — checks every pair (i, j) and computes area.
#   Space: O(1)   — only `best` and loop indices.


class BetterSolution:
    def solve(self, height: List[int]) -> int:
        return OptimalSolution().solve(height)


# Complexity (BetterSolution)
#   Time:  O(n) — delegates to two-pointer optimal.
#   Space: O(1) — no extra state beyond optimal call.


class OptimalSolution:
    def solve(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            best = max(best, area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return best


# Complexity (OptimalSolution)
#   Time:  O(n) — each pointer moves forward at most n times.
#   Space: O(1) — moving shorter wall never skips a better area.

