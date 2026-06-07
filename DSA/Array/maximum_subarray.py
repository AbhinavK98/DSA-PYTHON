"""
1. Maximum Subarray
Easy
Given an integer array nums, find the contiguous subarray (containing at least one number) with the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The contiguous subarray [4,-1,2,1] has the largest sum = 6.
Example 2:
Input: nums = [1]
Output: 1
Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""

from typing import List


def solution1_bruteforce(nums: List[int]) -> int:
    # Step 1: Initialize best sum to the first element.
    # Step 2: For each start index i, initialize a running total to 0.
    # Step 3: For each end index j from i to the end, add nums[j] to the running total.
    # Step 4: Update the best sum whenever the current running total exceeds it.
    # Step 5: After checking all subarrays, return the best sum found.
    # Time Complexity: O(n^2) because it considers every subarray starting point and extends it to every possible end point.
    # Space Complexity: O(1) because only a few variables are used.
    n = len(nums)
    best = nums[0]
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            best = max(best, s)
    return best


def solution2_average(nums: List[int]) -> int:
    # Step 1: Build a prefix sum array where prefix[i] is the sum of nums[0:i].
    # Step 2: For each pair of indices i < j, compute the sum of nums[i:j] as prefix[j] - prefix[i].
    # Step 3: Track the maximum subarray sum across all pairs.
    # Step 4: Return the maximum value found.
    # Time Complexity: O(n^2) because it compares every pair of prefix sums to compute subarray sums.
    # Space Complexity: O(n) because the prefix array stores n+1 cumulative sums.
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    best = nums[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            best = max(best, prefix[j] - prefix[i])
    return best


def solution3_optimal(nums: List[int]) -> int:
    # Step 1: Initialize current running maximum and global maximum to the first element.
    # Step 2: For each new value, decide whether to extend the previous subarray or start a new one at the current value by comparing current value with current value + previous running sum.
    # Step 3: Update the global maximum if the new running sum is larger.
    # Step 4: Continue until the end and return the global maximum.
    # Time Complexity: O(n) because it processes each number once with constant operations per number.
    # Space Complexity: O(1) because only a fixed number of variables are stored.
    current = maximum = nums[0]
    for value in nums[1:]:
        current = max(value, current + value)
        maximum = max(maximum, current)
    return maximum


# Pattern: Kadane's algorithm, a dynamic programming greedy method using current and global maxima.


if __name__ == "__main__":
    assert solution3_optimal([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert solution3_optimal([1]) == 1
    assert solution3_optimal([5,4,-1,7,8]) == 23
    print("maximum_subarray: all tests passed")
