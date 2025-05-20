"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:

i != j != k
nums[i] + nums[j] + nums[k] == 0
The solution set must not contain duplicate triplets.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
"""

from typing import List

def three_sum(nums: List):
    nums.sort()
    ans = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i+1, len(nums)-1

        while left < right:
            temp = nums[i] + nums[left] + nums[right]
            if temp == 0:
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif temp > 0:
                right -= 1
            else:
                left += 1
    return ans

print(three_sum([-1, 0, 1, 2, -1, -4]))