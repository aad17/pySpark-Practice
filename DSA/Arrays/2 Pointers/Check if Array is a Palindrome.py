"""
Given an array of integers arr, check if it reads the same forward and backward using the two pointers approach.

Return True if it is a palindrome, otherwise False.

Example:
Input: arr = [1, 2, 3, 2, 1]
Output: True

Input: arr = [1, 2, 3, 4]
Output: False
"""
from typing import List

def is_palindrome(arr: List):
    left, right = 0, len(arr) - 1

    while left <= right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome([1, 2, 3, 2, 1]))