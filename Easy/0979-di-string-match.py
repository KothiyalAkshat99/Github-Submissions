"""
Problem Name: DI String Match
Difficulty: Easy
Tags: Array, Two Pointers, String, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 18.7 MB
"""
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        ret = []

        for char in s:
            if char == "I":
                ret.append(low)
                low += 1
            else:
                ret.append(high)
                high -= 1
        
        return ret + [low]

