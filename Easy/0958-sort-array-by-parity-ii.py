"""
Problem Name: Sort Array By Parity II
Difficulty: Easy
Tags: Array, Two Pointers, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19 MB
"""
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1 # even and odd pointers
        n = len(nums)

        while i < n and j < n:
            # Move even pointer while it is satisfied
            while i < n and nums[i] % 2 == 0:
                i += 2
            
            while j < n and nums[j] % 2 == 1:
                j += 2
            
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
        
        return nums

