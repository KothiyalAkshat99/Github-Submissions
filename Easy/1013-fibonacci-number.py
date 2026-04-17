"""
Problem Name: Fibonacci Number
Difficulty: Easy
Tags: Math, Dynamic Programming, Recursion, Memoization
"""

"""
Submission 1
Language: python3
Runtime: 39 ms
Memory: 17.8 MB
"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        n -= 1
        x = 0
        a = 0
        b = 1
        while n:
            x = a + b
            n -= 1
            a = b
            b = x
        
        return x

