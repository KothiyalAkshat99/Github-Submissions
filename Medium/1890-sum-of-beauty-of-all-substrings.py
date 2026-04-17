"""
Problem Name: Sum of Beauty of All Substrings
Difficulty: Medium
Tags: Hash Table, String, Counting
"""

"""
Submission 1
Language: python3
Runtime: 6482 ms
Memory: 17.8 MB
"""
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ret = 0

        for i in range(n):
            hmap = {}
            for j in range(i, n):
                hmap[s[j]] = hmap.get(s[j], 0) + 1
                maxf = 0
                minf = 1000
                for key, val in hmap.items():
                    maxf = max(maxf, val)
                    minf = min(minf, val)
                ret += (maxf-minf)
        return ret

"""
Submission 2
Language: python3
Runtime: 1183 ms
Memory: 17.7 MB
"""
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ret = 0

        for i in range(n):
            hmap = {}
            for j in range(i, n):
                hmap[s[j]] = hmap.get(s[j], 0) + 1
                ret += max(hmap.values()) - min(hmap.values())
        return ret

