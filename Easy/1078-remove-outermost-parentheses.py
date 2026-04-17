"""
Problem Name: Remove Outermost Parentheses
Difficulty: Easy
Tags: String, Stack
"""

"""
Submission 1
Language: python3
Runtime: 7 ms
Memory: 18 MB
"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_count, close_count = 0, 0
        l = 0
        r = 0
        stk = []
        for r in range(len(s)):
            if s[r] == '(':
                open_count += 1
            else:
                close_count += 1
            
            if open_count == close_count:
                stk.append(s[l + 1 : r])
                #print(stk)
                l = r + 1
        
        ret = ""
        for i in stk:
            ret += i
        
        return ret

