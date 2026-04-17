"""
Problem Name: Find First and Last Position of Element in Sorted Array
Difficulty: Medium
Tags: Array, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.1 MB
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
    
    # leftBias = T/F. If True, we're looking for left-limit. If False, we're looking for right limit
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:    # Trying to find leftbound of target
                    r = m - 1
                else:           # To find rightbound of target
                    l = m + 1
        return i

