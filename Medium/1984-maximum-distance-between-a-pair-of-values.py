"""
Problem Name: Maximum Distance Between a Pair of Values
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 31 ms
Memory: 36.1 MB
"""
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0   # index for num1. Need to keep it AS LEFT as possible
        j = 1   # index for num2. Need to keep it as RIGHT as possible

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            j += 1
        
        return j - i - 1

"""
Submission 2
Language: python3
Runtime: 39 ms
Memory: 35.8 MB
"""
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0   # index for num1. Need to keep it AS LEFT as possible
        j = 0   # index for num2. Need to keep it as RIGHT as possible

        ret = 0
        while i < len(nums1) and j < len(nums2):
            if nums2[j] >= nums1[i]:
                j += 1
            else:
                i += 1
                j += 1
            
            ret = max(ret, j - i)
        
        return max(ret - 1, 0)

