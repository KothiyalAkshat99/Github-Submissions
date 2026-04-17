"""
Problem Name: Decode Ways
Difficulty: Medium
Tags: String, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 18 MB
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            if s[i] == "0":
                return 0
            
            ret = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                ret += dfs(i + 2)
            
            dp[i] = ret
            return ret
        
        return dfs(0)

