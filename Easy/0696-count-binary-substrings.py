"""
Problem Name: Count Binary Substrings
Difficulty: Easy
Tags: Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 71 ms
Memory: 18 MB
"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr = 1    # Considering current val count to be 1 initially
        prev = 0
        ret = 0

        # Starting from Index 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ret += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1

        return ret + min(prev, curr)

