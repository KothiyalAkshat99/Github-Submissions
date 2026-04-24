"""
Problem Name: Word Break
Difficulty: Medium
Tags: Array, Hash Table, String, Dynamic Programming, Trie, Memoization
"""

"""
Submission 1
Language: python3
Runtime: 2 ms
Memory: 18 MB
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]

"""
Submission 2
Language: python3
Runtime: 3 ms
Memory: 19.7 MB
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def dp(i: int):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            for j in range(i + 1, len(s) + 1):
                prefix = s[i : j]
                # If current substring is a valid word,
                # recursively call function with j (end of word).
                # Now for recursive call, j will be start of new word.
                # If it reaches end of string, returns True.
                if prefix in wordDict and dp(j):
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False
        
        return dp(0)

"""
Submission 3
Language: python3
Runtime: 3 ms
Memory: 19.3 MB
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] represents if substring s[0:i] can be segmented

        dp[0] = True    # Empty String base case

        for i in range(1, n + 1):
            for j in range(i):
                # If first part is valid AND second part is a word
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break   # Found valid segmentation at i, move to next i
        
        return dp[n]

"""
Submission 4
Language: python3
Runtime: 3 ms
Memory: 19.4 MB
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def recur(i: int):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            for j in range(i + 1, len(s) + 1):
                prefix = s[i:j] # Current word formed
                
                # If current substring in wordDict -> valid word
                # AND 
                # if the substring starting at j also returns TRUE
                if prefix in wordDict and \
                    recur(j):
                    memo[i] = True
                    return memo[i]
            
            memo[i] = False
            return memo[i]
        
        return recur(0)

