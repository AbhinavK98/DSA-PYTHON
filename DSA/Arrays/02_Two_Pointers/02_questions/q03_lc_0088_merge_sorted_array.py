"""LeetCode #88 - Merge Sorted Array.
Question Link: https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List


class BruteForce:
    def solve(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:m] = sorted(nums1[:m] + nums2[:n])


# Complexity (BruteForce)
#   Time:  O((m + n) log(m + n)) — concatenate then sort merged slice.
#   Space: O(m + n)             — temporary combined list before sort.


class BetterSolution:
    def solve(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged: List[int] = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        merged.extend(nums1[i:m])
        merged.extend(nums2[j:n])
        nums1[: m + n] = merged


# Complexity (BetterSolution)
#   Time:  O(m + n) — each element merged once via two pointers.
#   Space: O(m + n) — extra `merged` array before copying back.


class OptimalSolution:
    def solve(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, write = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1


# Complexity (OptimalSolution)
#   Time:  O(m + n) — fill from end; each element placed once.
#   Space: O(1)     — merge in-place using nums1's trailing empty slots.

