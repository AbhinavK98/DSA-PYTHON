"""
1. Subarray Sum Equals K
Medium
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""

from typing import List
from collections import defaultdict


def solution1_bruteforce(nums: List[int], k: int) -> int:
    # Step 1: Initialize count to 0.
    # Step 2: For each start index i, initialize current sum = 0.
    # Step 3: For each end index j from i to n-1, add nums[j] to current sum.
    # Step 4: If current sum equals k, increment count.
    # Step 5: Return count after all start/end pairs are considered.
    # Time Complexity: O(n^2) because it examines all subarrays starting at each index.
    # Space Complexity: O(1) because only a handful of variables are used.
    count = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                count += 1
    return count


def solution2_average(nums: List[int], k: int) -> int:
    # Step 1: Build prefix sums so prefix[i] is the sum of the first i elements.
    # Step 2: For each pair i < j, compute the subarray sum from i to j-1 as prefix[j] - prefix[i].
    # Step 3: Compare that difference to k and count matches.
    # Step 4: Return the total count.
    # Time Complexity: O(n^2) because it checks all prefix pair combinations.
    # Space Complexity: O(n) because it stores the prefix sums array.
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if prefix[j] - prefix[i] == k:
                count += 1
    return count


def solution3_optimal(nums: List[int], k: int) -> int:
    # Step 1: Initialize prefix_sum = 0 and a hashmap count of prefix sums seen.
    # Step 2: Add seen[0] = 1 before the loop to count subarrays starting at index 0.
    # Step 3: For each value, add it to prefix_sum.
    # Step 4: If prefix_sum - k has been seen before, it means a previous prefix_sum creates a subarray summing to k, so add its frequency to count.
    # Step 5: Increment the frequency of the current prefix_sum in the hashmap.
    # Step 6: Return count after scanning all values.
    # Time Complexity: O(n) because the array is scanned once and each hashmap lookup/update is O(1) on average.
    # Space Complexity: O(n) because the hashmap may store up to n different prefix sums.
    prefix_sum = 0
    count = 0
    seen = defaultdict(int)
    seen[0] = 1
    for value in nums:
        prefix_sum += value
        count += seen[prefix_sum - k]
        seen[prefix_sum] += 1
    return count


# Pattern: Prefix sums with hashmap, count previous sums that allow current subarray to equal k.


if __name__ == "__main__":
    assert solution3_optimal([1,1,1], 2) == 2
    assert solution3_optimal([1,2,3], 3) == 2
    print("subarray_sum_equals_k: all tests passed")
