"""LeetCode #73 - Set Matrix Zeroes.
Question Link: https://leetcode.com/problems/set-matrix-zeroes/
"""
from typing import List


class BruteForce:
    def solve(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in rows:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0

        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0


# Complexity (BruteForce)
#   Time:  O(m * n) scan + O(m * n) zeroing marked rows/cols.
#   Space: O(m + n) — sets storing which rows and columns to zero.


class BetterSolution:
    def solve(self, matrix: List[List[int]]) -> None:
        BruteForce().solve(matrix)


# Complexity (BetterSolution)
#   Time:  O(m * n) — same as brute force (placeholder delegation).
#   Space: O(m + n) — row/col marker sets.


class OptimalSolution:
    def solve(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_col_zero = False
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0


# Complexity (OptimalSolution)
#   Time:  O(m * n) — three passes: mark, apply, fix first row/col.
#   Space: O(1) — first row and column reused as zero markers.

