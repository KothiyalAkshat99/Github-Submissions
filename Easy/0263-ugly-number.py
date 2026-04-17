"""
Problem Name: Ugly Number
Difficulty: Easy
Tags: Math
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i
        
        return n == 1

