"""
1. Search in Rotated Sorted Array
Medium
Given a rotated sorted array nums and an integer target, return the index of target if it is present, or -1 if it is not.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1
"""

from typing import List


def solution1_bruteforce(nums: List[int], target: int) -> int:
    # Step 1: Loop through each index in nums from 0 to len(nums)-1.
    # Step 2: Compare nums[i] with the target at each step.
    # Step 3: Return i if the target is found, otherwise return -1 after the loop.
    # Time Complexity: O(n) because it may examine every element in the worst case.
    # Space Complexity: O(1) because it only uses index variables.
    for i, value in enumerate(nums):
        if value == target:
            return i
    return -1


def solution2_average(nums: List[int], target: int) -> int:
    # Step 1: Find the pivot where the sorted array was rotated using binary search.
    # Step 2: Decide whether the target is in the left sorted side or the right sorted side based on the pivot and endpoints.
    # Step 3: Run binary search on the chosen half to find the target.
    # Time Complexity: O(log n) because the pivot search and the binary search each take logarithmic time.
    # Space Complexity: O(1) because only pointer variables are used.
    n = len(nums)
    lo, hi = 0, n - 1
    while lo < hi and nums[lo] > nums[hi]:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    pivot = lo
    lo, hi = 0, n - 1
    if nums[pivot] <= target <= nums[hi]:
        lo = pivot
    else:
        hi = pivot - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def solution3_optimal(nums: List[int], target: int) -> int:
    # Step 1: Use binary search directly on the rotated array.
    # Step 2: At each step, determine which half of the array is sorted by comparing nums[lo] and nums[mid].
    # Step 3: Check whether the target lies within the sorted half. If yes, narrow the search to that half; otherwise search the other half.
    # Step 4: Continue until the target is found or the search interval becomes empty.
    # Time Complexity: O(log n) because the search range halves each iteration.
    # Space Complexity: O(1) because it uses only a few index variables.
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# Pattern: Modified binary search, determine the sorted half and decide where target lies.


if __name__ == "__main__":
    assert solution3_optimal([4,5,6,7,0,1,2], 0) == 4
    assert solution3_optimal([4,5,6,7,0,1,2], 3) == -1
    assert solution3_optimal([1], 0) == -1
    print("search_in_rotated_sorted_array: all tests passed")
