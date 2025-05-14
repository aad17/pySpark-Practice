"""
Problem: Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number also sorted in non-decreasing order.

Example:

Input: 
nums = [-4,-1,0,3,10]
Output: 
[0,1,9,16,100]

Input:
nums = [-7,-3,2,3,11]
Output:
[4,9,9,49,121]

Input:
nums = [-5,-3,-2,-1]
Output:
[1,4,9,25]

Example 4:
Input:
nums = [0,1,2,3]
Output:
[0,1,4,9]

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order
"""

from typing import List

def squares(nums: List):
    n = len(nums) 
    l, r = 0, n-1
    ans = [-1] * n
    pointer = n - 1

    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            ans[pointer] = nums[l] ** 2
            l += 1
        else:
            ans[pointer] = nums[r] ** 2
            r -= 1

        pointer -= 1
    
    return ans

print(squares([-4,-1,0,3,10]))