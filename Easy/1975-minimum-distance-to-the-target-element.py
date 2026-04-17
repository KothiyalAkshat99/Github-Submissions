"""
Problem Name: Minimum Distance to the Target Element
Difficulty: Easy
Tags: Array
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ret = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                ret = min(ret, abs(i - start))
            
        return ret

