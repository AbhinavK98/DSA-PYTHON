"""
1. Missing Number
Easy
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing.

Example 1:
Input: nums = [3,0,1]
Output: 2
Example 2:
Input: nums = [0,1]
Output: 2
"""

from typing import List


def solution1_bruteforce(nums: List[int]) -> int:
    # Step 1: For each value from 0 to n, check whether it appears in nums.
    # Step 2: If a value is not present, return it as the missing number.
    # Step 3: Stop as soon as the missing value is found.
    # Time Complexity: O(n^2) when using list membership checks, because each membership check scans the list in the worst case.
    # Space Complexity: O(1) because it uses only a few scalar variables.
    n = len(nums)
    for value in range(n + 1):
        if value not in nums:
            return value
    raise ValueError("No missing number")


def solution2_average(nums: List[int]) -> int:
    # Step 1: Build a set of all values in nums.
    # Step 2: Iterate from 0 to n and return the first value not found in the set.
    # Step 3: This works because exactly one number in the range is missing.
    # Time Complexity: O(n) because building the set is O(n) and each membership check is O(1).
    # Space Complexity: O(n) because the set stores all input values.
    n = len(nums)
    full = set(range(n + 1))
    return (full - set(nums)).pop()


def solution3_optimal(nums: List[int]) -> int:
    # Step 1: Set missing = n.
    # Step 2: For each index i and value v in nums, XOR missing with i and v.
    # Step 3: In the end, the XOR result equals the missing number because all present numbers and indices cancel out.
    # Time Complexity: O(n) because it scans nums once and performs constant-time XOR operations per element.
    # Space Complexity: O(1) because it only uses one accumulator variable.
    missing = len(nums)
    for i, value in enumerate(nums):
        missing ^= i ^ value
    return missing


# Pattern: XOR or set membership, use cancellation of values to find the missing number.


if __name__ == "__main__":
    assert solution3_optimal([3,0,1]) == 2
    assert solution3_optimal([0,1]) == 2
    print("missing_number: all tests passed")
