"""LeetCode #48 - Rotate Image.
Question Link: https://leetcode.com/problems/rotate-image/
"""
from typing import List


class BruteForce:
    def solve(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                rotated[c][n - 1 - r] = matrix[r][c]
        for r in range(n):
            for c in range(n):
                matrix[r][c] = rotated[r][c]


# Complexity (BruteForce)
#   Time:  O(n^2) — fill new matrix then copy back (n = side length).
#   Space: O(n^2) — full rotated copy before writing in-place.


class BetterSolution:
    def solve(self, matrix: List[List[int]]) -> None:
        OptimalSolution().solve(matrix)


# Complexity (BetterSolution)
#   Time:  O(n^2) — delegates to transpose + reverse.
#   Space: O(1) — in-place rotation.


class OptimalSolution:
    def solve(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


# Complexity (OptimalSolution)
#   Time:  O(n^2) — reverse O(n) rows + transpose visits each cell once.
#   Space: O(1) — 90° rotation via in-place row reverse + swap.

