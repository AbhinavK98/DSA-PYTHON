"""
1. Move Zeroes
Easy
Given an integer array nums, move all 0's to the end while maintaining the relative order of the non-zero elements.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]
Example 3:
Input: nums = [1,0,2,0,3]
Output: [1,2,3,0,0]
"""

from typing import List


def solution1_bruteforce(nums: List[int]) -> None:
    # Step 1: Create two new lists: one for nonzero elements and one for zeros.
    # Step 2: Iterate over nums and append each element to the appropriate list.
    # Step 3: Replace nums with the concatenation of nonzeros followed by zeros.
    # Time Complexity: O(n) because it scans the array once to partition it.
    # Space Complexity: O(n) because it allocates two temporary lists that together hold all elements.
    zeros = [x for x in nums if x == 0]
    nonzeros = [x for x in nums if x != 0]
    nums[:] = nonzeros + zeros


def solution2_average(nums: List[int]) -> None:
    # Step 1: Create a result list of zeros with the same length as nums.
    # Step 2: Traverse nums and copy each nonzero value into the next available position in result.
    # Step 3: Copy the result list back into nums if needed (or return it).
    # Time Complexity: O(n) because it scans the input once and writes each element at most once.
    # Space Complexity: O(n) because it uses a separate result list of the same size as nums.
    result = [0] * len(nums)
    insert = 0
    for value in nums:
        if value != 0:
            result[insert] = value
            insert += 1
    nums[:] = result


def solution3_optimal(nums: List[int]) -> None:
    # Step 1: Use a write pointer to keep track of the next position for a nonzero value.
    # Step 2: Iterate through nums and whenever a nonzero is found, write it to the write pointer and advance the pointer.
    # Step 3: After the scan, fill the remaining positions with zeros.
    # Time Complexity: O(n) because it processes each element once and performs a small constant number of operations per element.
    # Space Complexity: O(1) because it only uses a constant number of extra variables and modifies nums in-place.
    insert = 0
    for value in nums:
        if value != 0:
            nums[insert] = value
            insert += 1
    for i in range(insert, len(nums)):
        nums[i] = 0


# Pattern: Two pointers / in-place partition, move nonzero values forward and fill zeros at the end.


if __name__ == "__main__":
    arr = [0,1,0,3,12]
    solution3_optimal(arr)
    assert arr == [1,3,12,0,0]

    arr = [0]
    solution3_optimal(arr)
    assert arr == [0]

    arr = [1,0,2,0,3]
    solution3_optimal(arr)
    assert arr == [1,2,3,0,0]

    print("move_zeroes: all tests passed")
