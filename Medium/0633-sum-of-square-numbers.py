"""
Problem Name: Sum of Square Numbers
Difficulty: Medium
Tags: Math, Two Pointers, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 51 ms
Memory: 17.8 MB
"""
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))

        while left <= right:
            total = left ** 2 + right ** 2

            if total > c:
                right -= 1
            elif total < c:
                left += 1
            else:
                return True
        
        return False

