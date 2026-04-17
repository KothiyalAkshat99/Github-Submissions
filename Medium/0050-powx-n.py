"""
Problem Name: Pow(x, n)
Difficulty: Medium
Tags: Math, Recursion
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def findPow(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            ret = findPow(x, n // 2)
            ret = ret * ret

            if n % 2 == 1:
                return ret * x
            
            return ret
        
        ret = findPow(x, abs(n))

        if n >= 0:
            return ret
        
        return 1/ret

