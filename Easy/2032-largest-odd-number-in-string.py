"""
Problem Name: Largest Odd Number in String
Difficulty: Easy
Tags: Math, String, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 6 ms
Memory: 18.9 MB
"""
class Solution:
    def largestOddNumber(self, num: str) -> str:
        ret = ""
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 0:
                continue
            ret += num[0:i+1]
            break
        return ret

