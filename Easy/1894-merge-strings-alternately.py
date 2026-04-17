"""
Problem Name: Merge Strings Alternately
Difficulty: Easy
Tags: Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 48 ms
Memory: 17.8 MB
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ret = ""
        while i < len(word1) and i < len(word2):
            ret += word1[i] + word2[i]
            i += 1
        
        if i == len(word1):
            ret += word2[i:]
        elif i == len(word2):
            ret += word1[i:]
        
        return ret

