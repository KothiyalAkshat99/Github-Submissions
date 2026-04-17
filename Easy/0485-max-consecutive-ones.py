"""
Problem Name: Max Consecutive Ones
Difficulty: Easy
Tags: Array
"""

"""
Submission 1
Language: python3
Runtime: 31 ms
Memory: 20.2 MB
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] != 1 or i+1 == len(nums):
                maxc = max(maxc, count)
                count = 0

        return maxc

