"""
Question: Two Sum II - Input Array Is Sorted
LeetCode: #167
Question Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: Medium
Pattern: Two pointers on sorted array
"""

from typing import List


class BruteForce:
    def solve(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []


# Complexity (BruteForce)
#   Time:  O(n^2) — nested loops try every pair in the sorted array.
#   Space: O(1)   — only index variables.


class BetterSolution:
    def solve(self, numbers: List[int], target: int) -> List[int]:
        # Hash map also works, but uses extra space.
        seen = {}
        for i, value in enumerate(numbers):
            need = target - value
            if need in seen:
                return [seen[need] + 1, i + 1]
            seen[value] = i
        return []


# Complexity (BetterSolution)
#   Time:  O(n) — one pass with O(1) hash map lookups.
#   Space: O(n) — map stores seen values (works but ignores sorted order).


class OptimalSolution:
    def solve(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            if current < target:
                left += 1
            else:
                right -= 1
        return []


# Complexity (OptimalSolution)
#   Time:  O(n) — left and right move at most n steps total.
#   Space: O(1) — exploits sorted input; no extra data structure.


if __name__ == '__main__':
    print(OptimalSolution().solve([2, 7, 11, 15], 9))

