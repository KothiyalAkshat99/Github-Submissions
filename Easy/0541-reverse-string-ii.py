"""
Problem Name: Reverse String II
Difficulty: Easy
Tags: Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18 MB
"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)

        for i in range(0, len(chars), 2*k):
            chars[i:i+k] = reversed(chars[i:i+k])
        
        return "".join(chars)

