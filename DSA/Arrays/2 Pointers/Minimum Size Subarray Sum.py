"""
Problem: Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray of which the sum is greater than or equal to target. 
If there is no such subarray, return 0.

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""

from typing import List

def min_subarr_sum(target: int, nums: List):
    window = 0
    left = 0
    ans = float('inf')
    for right in range(len(nums)):
        window += nums[right]
        while window >= target:
            ans = min(ans, right - left + 1)
            window -= nums[left]
            left += 1
    return ans if ans != float('inf') else 0

print(min_subarr_sum(7, [2,3,1,2,4,3]))