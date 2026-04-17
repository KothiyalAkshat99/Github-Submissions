"""
Problem Name: Rotate String
Difficulty: Easy
Tags: String, String Matching
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        if len(s) != len(goal):
            return False
        
        self_concat = s + s

        return self_concat.find(goal) != -1

