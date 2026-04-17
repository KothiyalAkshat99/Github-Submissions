"""
Problem Name: Sqrt(x)
Difficulty: Easy
Tags: Math, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.4 MB
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l, r = 1, x // 2

        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                l = mid + 1
            else:
                r = mid - 1
        
        return r

