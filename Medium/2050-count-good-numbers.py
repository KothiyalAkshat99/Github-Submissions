"""
Problem Name: Count Good Numbers
Difficulty: Medium
Tags: Math, Recursion
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        # Fast exponentiation to calculate x^y % mod

        def quickmul(x, y) -> int:
            ret, mul = 1, x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                y //= 2
            return ret
        

        # 5*(n+1)/2 even indices in a string of length n
        # 5 even indices digits - 0, 2, 4, 6, 8
        # 4*(n)/2 odd indices in a string of length n
        # 4 odd indices digit - 2, 3, 5, 7
        return quickmul(5, (n+1)//2) * quickmul(4, n//2) % mod

