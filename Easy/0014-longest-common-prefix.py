"""
Problem Name: Longest Common Prefix
Difficulty: Easy
Tags: Array, String, Trie
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return ret
            ret += strs[0][i]
        
        return ret

