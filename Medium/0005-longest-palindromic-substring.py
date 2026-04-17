"""
Problem Name: Longest Palindromic Substring
Difficulty: Medium
Tags: Two Pointers, String, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 313 ms
Memory: 18 MB
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        retlen = 0

        # We're considering each position to be the center of a supposed palindrome
        # Then we're gonna expand in either directions to find the \
        # length of palindrome that can be formed
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > retlen:
                    ret = s[l : r + 1]
                    retlen = r - l + 1
                
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > retlen:
                    ret = s[l : r + 1]
                    retlen = r - l + 1
                l -= 1
                r += 1
        
        return ret

"""
Submission 2
Language: python3
Runtime: 263 ms
Memory: 19.4 MB
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        n = len(s)
        ret = ""
        retlen = 0

        for i in range(n):
            l = i
            r = i
            
            # For Odd Length
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > retlen:
                    ret = s[l : r + 1]
                    retlen = r - l + 1
                
                l -= 1
                r += 1
            
            
            # For EVEN Length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > retlen:
                    ret = s[l : r + 1]
                    retlen = r - l + 1
                
                l -= 1
                r += 1
        
        return ret

