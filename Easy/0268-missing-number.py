"""
Problem Name: Missing Number
Difficulty: Easy
Tags: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 18.8 MB
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in range(0, len(nums)+1):
            sum += i
        
        numsum = 0
        for i in nums:
            numsum += i
        
        return sum - numsum

