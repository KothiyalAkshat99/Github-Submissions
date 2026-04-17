"""
Problem Name: Move Zeroes
Difficulty: Easy
Tags: Array, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 1 ms
Memory: 18.8 MB
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        l, r = 0, 0
        while r < len(nums):
            if nums[r]:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
            r += 1
        
        return

