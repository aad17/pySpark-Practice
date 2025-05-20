"""
Problem: Find Maximum Average Subarray of Length k
Given an array nums of n integers and an integer k, find the contiguous subarray of length k 
that has the maximum average value, and return this value.

You must solve it in O(n) time complexity.

Example:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Max average is (12 + -5 + -6 + 50) / 4 = 51 / 4 = 12.75

✅ Test Case 1:
Input:
nums = [1, 12, -5, -6, 50, 3], k = 4
Output:
12.75

✅ Test Case 2:
Input:
nums = [5, 5, 5, 5, 5], k = 3
Output:
5.0

✅ Test Case 3:
Input:
nums = [-1, -12, -5, -6, -50], k = 2
Output:
-3.0 (from [-1, -2])

Correction: Should be -6.0 (from [-5, -6])
Let’s recalculate:
Max average from [-1, -12] = -6.5, [-12, -5] = -8.5, [-5, -6] = -5.5, [-6, -50] = -28
→ Max = -5.5

✅ Correct Output: -5.5

✅ Test Case 4:
Input:
nums = [0, 4, 0, 3, 2], k = 2
Output:
3.5
"""

from typing import List

def avg_subarr_of_k(nums: List, k: int):
    window = sum(nums[:k])
    window_avg = window / k
    ans = window_avg

    for right in range(k, len(nums)):
        left = right - k
        window -= nums[left]
        window += nums[right]
        window_avg = window / k
        ans = max(ans, window_avg)
    return ans

print(avg_subarr_of_k([5, 5, 5, 5, 5], 3))
