"""
Problem Name: Concatenation of Array
Difficulty: Easy
Tags: Array, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 18 MB
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ret = []
        for _ in range(2):
            for num in nums:
                ret.append(num)
        
        return ret

