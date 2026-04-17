"""
Problem Name: Valid Parenthesis String
Difficulty: Medium
Tags: String, Dynamic Programming, Stack, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        ast = []

        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stk.append(i)
            elif c == "*":
                ast.append(i)
            else:
                if stk:
                    stk.pop()
                elif ast:
                    ast.pop()
                else:
                    return False
        
        while stk and ast:
            # if remaining asterisk is before remaining OPEN bracket
            if stk.pop() > ast.pop():
                return False
        
        return not stk

