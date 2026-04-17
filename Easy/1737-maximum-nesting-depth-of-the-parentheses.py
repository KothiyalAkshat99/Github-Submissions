"""
Problem Name: Maximum Nesting Depth of the Parentheses
Difficulty: Easy
Tags: String, Stack
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        maxc = 0
        for i in s:
            if i == "(":
                c += 1
            elif i == ")":
                maxc = max(maxc, c)
                c -= 1
        
        print(maxc)
        return maxc

