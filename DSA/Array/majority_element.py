"""
1. Majority Element
Easy
Given an array of size n, find the majority element that appears more than n/2 times.

Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List


def solution1_bruteforce(nums: List[int]) -> int:
    # Step 1: For each distinct candidate in nums, count how many times it appears.
    # Step 2: Compare the count to n // 2.
    # Step 3: Return the candidate if its count exceeds half the array length.
    # Time Complexity: O(n^2) in the worst case because counting a candidate may scan the whole input for each distinct value.
    # Space Complexity: O(1) if not storing distinct values, or O(n) if using a temporary set for distinct candidates.
    n = len(nums)
    for value in set(nums):
        if nums.count(value) > n // 2:
            return value
    raise ValueError("No majority element")


def solution2_average(nums: List[int]) -> int:
    # Step 1: Build a dictionary mapping each value to its frequency in nums.
    # Step 2: Iterate through the dictionary to find the value whose frequency is greater than n // 2.
    # Step 3: Return that value.
    # Time Complexity: O(n) because counting values is linear and the dictionary inspection is proportional to the number of distinct values.
    # Space Complexity: O(n) because the dictionary may store every distinct value.
    counts = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    for value, count in counts.items():
        if count > len(nums) // 2:
            return value
    raise ValueError("No majority element")


def solution3_optimal(nums: List[int]) -> int:
    # Step 1: Initialize candidate to None and count to 0.
    # Step 2: For each number in nums, if count is 0 set candidate to that number.
    # Step 3: If the number equals candidate increment count, otherwise decrement count.
    # Step 4: The final candidate is the majority because majority occurrences outweigh all others.
    # Time Complexity: O(n) because it traverses nums once.
    # Space Complexity: O(1) because it uses only two variables for candidate and count.
    candidate = None
    count = 0
    for value in nums:
        if count == 0:
            candidate = value
        count += 1 if value == candidate else -1
    return candidate


# Pattern: Boyer-Moore voting algorithm, track a candidate and cancel out non-majority values.


if __name__ == "__main__":
    assert solution3_optimal([3,2,3]) == 3
    assert solution3_optimal([2,2,1,1,1,2,2]) == 2
    print("majority_element: all tests passed")
