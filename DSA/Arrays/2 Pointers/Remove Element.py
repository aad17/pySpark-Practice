"""
Given an integer array nums and an integer val, remove all occurrences of val in-place, 
and return the new length of the array. The relative order of the elements can be changed.

You must do this with O(1) extra space.

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

"""

from typing import List

def remove_elem(nums: List, val: int):
    non_elem = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i], nums[non_elem] = nums[non_elem], nums[i]
            non_elem += 1
    return non_elem

print(remove_elem([0,1,2,2,3,0,4,2], 2))