"""
Problem Name: Sentence Similarity III
Difficulty: Medium
Tags: Array, Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        start, end1, end2 = 0, len(s1) - 1, len(s2) - 1

        # If words in s1 more than s2, swap them and return answer
        # Constructing solution considering len(s1) < len(s2) hence swapping
        if len(s1) > len(s2):
            return self.areSentencesSimilar(sentence2, sentence1)
        
        # Find max prefix length
        while start < len(s1) and s1[start] == s2[start]:
            start += 1
        
        # Find max suffix length
        while end1 >= 0 and s1[end1] == s2[end2]:
            end1 -= 1
            end2 -= 1
        
        # end of array reached for s1. Hence one of the arrays completely consumed
        return end1 < start

