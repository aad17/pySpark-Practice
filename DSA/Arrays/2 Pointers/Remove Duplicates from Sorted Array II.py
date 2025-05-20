"""
Problem: Remove Duplicates from Sorted Array II
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element 
appears at most twice.

Return the new length of nums after removing extra duplicates.
Do not allocate extra space — you must do this by modifying the input array in-place with O(1) extra memory.

Example:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
"""

from typing import List

def remove_dups_2(nums: List):
    write = 0

    for read in range(len(nums)):
        if write < 2 or nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
    return write

print(remove_dups_2([0,0,1,1,1,1,2,3,3]))