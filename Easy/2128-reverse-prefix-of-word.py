"""
Problem Name: Reverse Prefix of Word
Difficulty: Easy
Tags: Two Pointers, String, Stack
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        if i != -1:
            ret = word[:i+1][::-1] + "" + word[i + 1:]
            word = ret
        return word

