"""
Problem Name: Number of Steps to Reduce a Number to Zero
Difficulty: Easy
Tags: Math, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 35 ms
Memory: 16.6 MB
"""
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num==0:
            return 0
        global c
        c = 0
        while True:
            if num%2==0:
                num/=2
            else:
                num-=1
            c+=1
            if num==0:
                break
        return c

