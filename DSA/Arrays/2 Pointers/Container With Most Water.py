"""
Problem: Container With Most Water
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the i-th line are at (i, 0) and (i, height[i]).

Find two lines that, together with the x-axis, form a container that holds the most water.

Return the maximum amount of water a container can store.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

"""
from typing import List

def container(height: List):
    l, r = 0, len(height) - 1
    curr_level = min(height[l], height[r]) * (r-l)
    while l < r:
        curr_level = max(curr_level, min(height[l], height[r]) * (r-l))
        if height[l] > height[r]:
            r -= 1
        elif height[r] > height[l]:
            l += 1
        else:
            r -= 1
            l += 1
    
    return curr_level

print(container([1,8,6,2,5,4,8,3,7]))