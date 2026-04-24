"""
Problem Name: Two Furthest Houses With Different Colors
Difficulty: Easy
Tags: Array, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.2 MB
"""
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        l = 0
        r = n - 1

        max_dist = 0

        # Compare houses against FIRST And LAST house.
        # Against last house -> find the first house which is different colored
        for i in range(n):
            if colors[i] != colors[n - 1]:
                left = i    # Found first different color at i, so break
                break
        
        # Against first house
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                right = i
                break
        
        # Max dist = either from first house or from last house
        return max(right - 0, n - 1 - left)

