"""
Problem Name: Number of Adjacent Elements With the Same Color
Difficulty: Medium
Tags: Array
"""

"""
Submission 1
Language: python3
Runtime: 83 ms
Memory: 50 MB
"""
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        count = 0

        ret = []

        for i, c in queries:
            prev = colors[i-1] if i > 0 else 0
            nxt = colors[i+1] if i < n-1 else 0

            if colors[i] and colors[i] == prev:
                count -= 1
            if colors[i] and colors[i] == nxt:
                count -= 1
            
            colors[i] = c

            if colors[i] == prev:
                count +=  1
            if colors[i] == nxt:
                count += 1
            
            ret.append(count)
        return ret

