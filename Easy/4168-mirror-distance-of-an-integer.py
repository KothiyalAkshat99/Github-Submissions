"""
Problem Name: Mirror Distance of an Integer
Difficulty: Easy
Tags: Math
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.1 MB
"""
class Solution:
    def mirrorDistance(self, n: int) -> int:
        n_reverse = 0
        m = n
        while m:
            n_reverse = n_reverse * 10 + m % 10
            m = m // 10
        
        return abs(n - n_reverse)

