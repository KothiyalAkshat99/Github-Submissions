"""
Problem Name: Neighboring Bitwise XOR
Difficulty: Medium
Tags: Array, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 48 ms
Memory: 22.2 MB
"""
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        s = 0
        for i in derived:
            s = s ^ i
        
        if s == 0:
            return True
        else:
            return False

