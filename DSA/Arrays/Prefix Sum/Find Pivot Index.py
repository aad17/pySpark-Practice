"""
Description:
Given an array of integers nums, return the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left is equal to the sum of all the numbers 
strictly to the right.

If no such index exists, return -1. If there are multiple pivot indexes, return the left-most one.

Function Signature:

def pivotIndex(nums: List[int]) -> int:
Example:

Input: nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
Left sum = 1 + 7 + 3 = 11
Right sum = 5 + 6 = 11
Constraints:

1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
"""

from typing import List

def pivotIndex(nums: List[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0

    for i, x in enumerate(nums):
        if left_sum == total_sum - left_sum - x:
            return i
        left_sum += x
    
    return -1

print(pivotIndex([1, 7, 3, 6, 5, 6]))