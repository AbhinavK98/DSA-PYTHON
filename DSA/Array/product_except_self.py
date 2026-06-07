"""
1. Product of Array Except Self
Medium
Given an array nums, return an array answer such that answer[i] is the product of all the elements of nums except nums[i]. Solve without division and in O(n).

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from typing import List


def solution1_bruteforce(nums: List[int]) -> List[int]:
    # Step 1: Create an empty output list.
    # Step 2: For each index i, initialize product to 1 and multiply every element nums[j] for j != i.
    # Step 3: Append the product for index i to the output list.
    # Step 4: Return the output list after processing all indices.
    # Time Complexity: O(n^2) because for each of the n positions it multiplies up to n-1 other values.
    # Space Complexity: O(n) because the output list stores n products.
    n = len(nums)
    output = []
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        output.append(prod)
    return output


def solution2_average(nums: List[int]) -> List[int]:
    # Step 1: Count the number of zeros and compute the product of all nonzero numbers.
    # Step 2: If more than one zero exists, every output entry is zero.
    # Step 3: If exactly one zero exists, the output is zero everywhere except at the zero position, where it is the product of all nonzero numbers.
    # Step 4: If there are no zeros, each output is total_product // nums[i].
    # Time Complexity: O(n) because it scans the input once to compute the product and then once more to build the output.
    # Space Complexity: O(n) because the output list holds n values and only constant extra storage is used besides that.
    total_product = 1
    zero_count = 0
    for value in nums:
        if value == 0:
            zero_count += 1
        else:
            total_product *= value
    result = []
    for value in nums:
        if zero_count > 1:
            result.append(0)
        elif zero_count == 1:
            result.append(0 if value != 0 else total_product)
        else:
            result.append(total_product // value)
    return result


def solution3_optimal(nums: List[int]) -> List[int]:
    # Step 1: Initialize answer list with 1s.
    # Step 2: Compute prefix products from left to right and store them in answer[i] as the product of all elements before i.
    # Step 3: Compute suffix products from right to left and multiply them into answer[i] so each position holds product of elements before and after i.
    # Step 4: Return answer without using division.
    # Time Complexity: O(n) because it makes two linear passes over the input array.
    # Space Complexity: O(1) extra space beyond the output array because no additional arrays proportional to input size are used.
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


# Pattern: Prefix and suffix product scan, combine left and right products for each index.


if __name__ == "__main__":
    assert solution3_optimal([1,2,3,4]) == [24,12,8,6]
    assert solution3_optimal([-1,1,0,-3,3]) == [0,0,9,0,0]
    print("product_except_self: all tests passed")
