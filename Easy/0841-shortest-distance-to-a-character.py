"""
Problem Name: Shortest Distance to a Character
Difficulty: Easy
Tags: Array, Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.8 MB
"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # 2 Pass - L to R and R to L
        ret = [-1] * len(s)
        prev = -10**5
        for i in range(len(s)):
            if s[i] == c:
                prev = i
            ret[i] = i - prev
        
        prev = 10**5
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                prev = i
            ret[i] = min(ret[i], prev-i)
        
        return ret

