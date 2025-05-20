"""
Problem: Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

✅ Test Case 1:
Input:
nums = [0, 1, 0, 3, 12]
Output:
[1, 3, 12, 0, 0]

✅ Test Case 2:
Input:
nums = [0, 0, 0, 1]
Output:
[1, 0, 0, 0]

✅ Test Case 3:
Input:
nums = [1, 2, 3, 4]
Output:
[1, 2, 3, 4] (No zeros, unchanged)

✅ Test Case 4:
Input:
nums = [0, 0, 0, 0]
Output:
[0, 0, 0, 0] (All zeros, unchanged)

✅ Test Case 5:
Input:
nums = [4, 0, 5, 0, 6, 7]
Output:
[4, 5, 6, 7, 0, 0]
"""

from typing import List

def move_zeroes(nums: List):
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1
        fast += 1
    return nums

print(move_zeroes([0, 1, 0, 3, 12]))
