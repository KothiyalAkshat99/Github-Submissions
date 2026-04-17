"""
Problem Name: Remove Element
Difficulty: Easy
Tags: Array, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k

