"""
1. Container With Most Water
Medium
Given n non-negative integers height, find two lines that together with the x-axis form a container with the most water.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Example 2:
Input: height = [1,1]
Output: 1
"""

from typing import List


def solution1_bruteforce(height: List[int]) -> int:
    # Step 1: Consider every pair of left and right lines (i, j).
    # Step 2: Compute the height as min(height[i], height[j]) and width as j - i.
    # Step 3: Calculate area = height * width and track the maximum.
    # Step 4: Return the maximum area found.
    # Time Complexity: O(n^2) because it checks every pair of lines for possible area.
    # Space Complexity: O(1) because it only stores a couple of variables.
    best = 0
    n = len(height)
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, min(height[i], height[j]) * (j - i))
    return best


def solution2_average(height: List[int]) -> int:
    # Step 1: Initialize left pointer at 0 and right pointer at len(height)-1.
    # Step 2: Compute area from the lines at the pointers.
    # Step 3: Move the pointer at the shorter line inward, because only a taller line can increase area.
    # Step 4: Repeat until left and right meet.
    # Time Complexity: O(n) because each pointer moves at most n steps inward.
    # Space Complexity: O(1) because only the pointers and max area variable are stored.
    i, j = 0, len(height) - 1
    best = 0
    while i < j:
        best = max(best, min(height[i], height[j]) * (j - i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return best


def solution3_optimal(height: List[int]) -> int:
    # Step 1: Start with left = 0 and right = len(height)-1.
    # Step 2: At each step, compute the area and update the maximum if necessary.
    # Step 3: Move the pointer at the smaller height toward the center to potentially find a taller boundary.
    # Step 4: Continue until left and right meet and return the largest area found.
    # Time Complexity: O(n) because the pointers move inward in a single scan.
    # Space Complexity: O(1) because it uses only a few variables.
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


# Pattern: Two pointers, move the smaller side inward to maximize area.


if __name__ == "__main__":
    assert solution3_optimal([1,8,6,2,5,4,8,3,7]) == 49
    assert solution3_optimal([1,1]) == 1
    print("container_with_most_water: all tests passed")
