"""
Problem Name: Decode String
Difficulty: Medium
Tags: String, Stack, Recursion
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.5 MB
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        ret = ""
        for i in range(len(s)):
            if s[i] != ']':
                stk.append(s[i])
                continue
            
            substr = ""
            while stk[-1] != '[':
                substr = stk.pop() + substr
            stk.pop() # Popping opening bracket

            k = ""
            # Need to get k from stack now
            while stk and stk[-1].isdigit():
                k = stk.pop() + k
            
            stk.append(int(k) * substr) # Adding processed substring back to stack
        
        return "".join(stk)

