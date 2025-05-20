"""
Problem: Merge Two Sorted Arrays
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2, respectively.

Merge nums2 into nums1 as one sorted array in-place. nums1 has enough space (size that is m + n) 
to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
Output:
[1,2,2,3,5,6]

Input:
nums1 = [1], m = 1
nums2 = [], n = 0
Output:
[1]

Input:
nums1 = [0], m = 0
nums2 = [1], n = 1
Output:
[1]

Input:
nums1 = [2,0], m = 1
nums2 = [1], n = 1
Output:
[1,2]
"""

from typing import List

def merge_sorted_arrays(nums1: List, m: int, nums2: List, n: int):
    p1, p2, p = m - 1, n - 1, m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If nums2 still has remaining elements
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

    return nums1

print(merge_sorted_arrays([1,2,3,0,0,0], 3, [2,5,6], 3))