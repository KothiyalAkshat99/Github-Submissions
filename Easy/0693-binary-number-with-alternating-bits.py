"""
Problem Name: Binary Number with Alternating Bits
Difficulty: Easy
Tags: Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.2 MB
"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True

        prev = -1

        while n:
            curr = n % 2
            if prev == curr:
                return False
            n //= 2
            prev = curr
        
        return True

