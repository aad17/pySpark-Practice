"""
You are given an integer array nums sorted in non-decreasing order. 
Remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Modify the array in-place and return the number of unique elements.

Input:
nums = [1, 1, 2]
Output:
2, nums = [1, 2, _]

Input:
nums = [0,0,1,1,1,2,2,3,3,4]
Output:
5, nums = [0,1,2,3,4,_,_,_,_,_]

Input:
nums = [1,2,3,4,5]
Output:
5, nums = [1,2,3,4,5]

Input:
nums = [2,2,2,2,2]
Output:
1, nums = [2,_]
"""
from typing import List

def remove_duplicates(nums: List[int]):
    n = len(nums)

    if n == 1:
        return 0, nums
    
    l = 0

    for r in range(1, n):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]

    return l + 1, nums

print(remove_duplicates([2,2,2,2,2]))
