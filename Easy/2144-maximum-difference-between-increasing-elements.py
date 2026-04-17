"""
Problem Name: Maximum Difference Between Increasing Elements
Difficulty: Easy
Tags: Array
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # Cannot sort since restriction on indices

        maxDiff = -1
        minNum = nums[0] # This will be minimum number up till the point another number < this is found.

        for i in range(1, len(nums)):
            if nums[i] > minNum:
                maxDiff = max(nums[i] - minNum, maxDiff)
            elif nums[i] < minNum:
                minNum = nums[i]
        
        return maxDiff

