"""
1. Two Sum
Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List, Tuple


def solution1_bruteforce(nums: List[int], target: int) -> Tuple[int, int]:
    # Step 1: Get the input length n.
    # Step 2: Iterate i from 0 to n-2 as the first index.
    # Step 3: For each i, iterate j from i+1 to n-1 as the second index.
    # Step 4: Add nums[i] + nums[j] and compare with target.
    # Step 5: If the sum equals target, return the index pair immediately.
    # Time Complexity: O(n^2) because for each i you may examine all remaining j values, yielding roughly n*(n-1)/2 pair checks.
    # Space Complexity: O(1) because the algorithm only stores a few variables and does not allocate extra space proportional to n.
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    raise ValueError("No solution")


def solution2_average(nums: List[int], target: int) -> Tuple[int, int]:
    # Step 1: Build a hash map mapping value -> index for all elements in nums.
    # Step 2: Iterate through nums again and for each value compute complement = target - value.
    # Step 3: If the complement is in the map and is not the same index, then the pair has been found.
    # Step 4: Return the indices when the matching complement is discovered.
    # Time Complexity: O(n) average-case because both the map construction and the complement checks each take linear time when hash operations are O(1).
    # Space Complexity: O(n) because the hash map stores one entry for each element in nums.
    comp = {}
    for i, v in enumerate(nums):
        comp[v] = i
    for i, v in enumerate(nums):
        need = target - v
        if need in comp and comp[need] != i:
            return (i, comp[need])
    raise ValueError("No solution")


def solution3_optimal(nums: List[int], target: int) -> Tuple[int, int]:
    # Step 1: Initialize an empty hash map to store complements needed for future numbers.
    # Step 2: Loop through nums once and for each current value v compute the required complement target - v.
    # Step 3: If the current value is already found as a required complement from an earlier element, return the stored index and the current index.
    # Step 4: Otherwise, store the current needed complement with the current index so later values can match it.
    # Time Complexity: O(n) because each number is visited once and hash lookups are O(1) on average.
    # Space Complexity: O(n) because the complement map may store up to n entries in the worst case.
    comp = {}
    for i, v in enumerate(nums):
        if v in comp:
            return (comp[v], i)
        comp[target - v] = i
    raise ValueError("No solution")


# Pattern: Hash map, use complements to find the pair in one pass.


if __name__ == "__main__":
    assert solution3_optimal([2, 7, 11, 15], 9) == (0, 1)
    assert solution3_optimal([3, 2, 4], 6) == (1, 2)
    assert solution3_optimal([3, 3], 6) == (0, 1)
    print("two_sum: all tests passed")
