"""
Problem: Subarray Product Less Than K
Given an array of positive integers nums and an integer k, return the number of contiguous subarrays where the product of 
all elements in the subarray is less than k.

Example:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: Subarrays: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
"""

from typing import List

def subarr_prod(nums: List, k: int):
    left = 0
    ans = 0
    window = 1
    for right in range(len(nums)):
        window *= nums[right]
        while window >= k:
            window //= nums[left]
            left += 1
        ans += (right - left + 1)
    return ans

print(subarr_prod([10, 5, 2, 6], 100))