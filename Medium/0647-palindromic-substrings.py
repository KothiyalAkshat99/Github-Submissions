"""
Problem Name: Palindromic Substrings
Difficulty: Medium
Tags: Two Pointers, String, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 109 ms
Memory: 17.9 MB
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        ret = 0
        n = len(s)

        def countPalindromes(s, l, r):
            c = 0
            while l >= 0 and r < n and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
            return c
        
        for i in range(n):
            ret += countPalindromes(s, i, i)
            ret += countPalindromes(s, i, i+1)
    
        return ret

"""
Submission 2
Language: python3
Runtime: 111 ms
Memory: 19.2 MB
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        n = len(s)
        #hashmap = {}
        ret = 0

        for i in range(n):
            # Odd
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                ret += 1
                l -= 1
                r += 1

            # Even
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                ret += 1
                l -= 1
                r += 1
        
        return ret

