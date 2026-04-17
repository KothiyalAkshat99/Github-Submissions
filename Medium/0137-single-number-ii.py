"""
Problem Name: Single Number II
Difficulty: Medium
Tags: Array, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.1 MB
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Concept of BUCKETS

        ones, twos = 0, 0

        for i in nums:
            ones ^= (i & ~twos)
            twos ^= (i & ~ones)
        
        return ones

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19.1 MB
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0

        for i in nums:
            ones = (ones ^ i) & (~twos)
            twos = (twos ^ i) & (~ones)
        
        return ones

