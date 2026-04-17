"""
Problem Name: Reverse Words in a String III
Difficulty: Easy
Tags: Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18.3 MB
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)

