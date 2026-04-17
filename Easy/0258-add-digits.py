"""
Problem Name: Add Digits
Difficulty: Easy
Tags: Math, Simulation, Number Theory
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        digit = 0
        n = num
        while n > 0:
            digit += n % 10
            n = n // 10
            if n == 0:
                n = digit
                digit = 0
                if n // 10 == 0:
                    return n

