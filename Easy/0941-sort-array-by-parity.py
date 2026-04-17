"""
Problem Name: Sort Array By Parity
Difficulty: Easy
Tags: Array, Two Pointers, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 18.4 MB
"""
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1:
            return nums
        
        left = 0
        right = len(nums) - 1

        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 != 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums

