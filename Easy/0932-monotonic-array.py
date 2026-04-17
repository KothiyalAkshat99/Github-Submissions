"""
Problem Name: Monotonic Array
Difficulty: Easy
Tags: Array
"""

"""
Submission 1
Language: python3
Runtime: 27 ms
Memory: 29.1 MB
"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True
        
        asc = True
        desc = True

        for i in range(1, len(nums)):
            if not asc and not desc:
                return False
            
            if nums[i] < nums[i - 1]:
                asc = False
            if nums[i] > nums[i - 1]:
                desc = False
        
        return asc or desc

