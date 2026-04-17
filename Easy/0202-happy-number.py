"""
Problem Name: Happy Number
Difficulty: Easy
Tags: Hash Table, Math, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18 MB
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        
        hashset = set()

        while n not in hashset:
            hashset.add(n)

            x = 0
            while n:
                digit = n % 10
                n = n // 10
                x = x + digit ** 2
            n = x
            
            if n == 1:
                return True
        
        return False

