"""
Problem Name: Binary Search
Difficulty: Easy
Tags: Array, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18.7 MB
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while(i<=j):
            k = (i + j) // 2
            if target > nums[k]:
                i = k+1
            elif target < nums[k]:
                j = k-1
            else:
                return k
        
        return -1

