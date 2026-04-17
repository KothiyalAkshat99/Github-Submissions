"""
Problem Name: Generate Parentheses
Difficulty: Medium
Tags: String, Dynamic Programming, Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        
        def recur(openP, closeP, st):
            if openP == closeP and openP + closeP == n*2:
                ret.append(st)
                return
            
            if openP < n:
                recur(openP + 1, closeP, st + "(")
            if closeP < openP:
                recur(openP, closeP + 1, st + ")")
        
        recur(0, 0, "")

        return ret

