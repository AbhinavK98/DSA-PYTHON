"""LeetCode #238 - Product of Array Except Self.
Question Link: https://leetcode.com/problems/product-of-array-except-self/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            answer.append(product)
        return answer


# Complexity (BruteForce)
#   Time:  O(n^2) — for each index i, multiply all other n-1 elements.
#   Space: O(n)   — output array.


class BetterSolution:
    def solve(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        return [left[i] * right[i] for i in range(n)]


# Complexity (BetterSolution)
#   Time:  O(n) — two prefix/suffix passes + O(n) combine.
#   Space: O(n) — separate left[] and right[] arrays.


class OptimalSolution:
    def solve(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# Complexity (OptimalSolution)
#   Time:  O(n) — prefix pass left-to-right, suffix pass right-to-left.
#   Space: O(1) extra — output array excluded; only prefix/suffix scalars.
