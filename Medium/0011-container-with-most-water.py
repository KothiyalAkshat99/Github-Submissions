"""
Problem Name: Container With Most Water
Difficulty: Medium
Tags: Array, Two Pointers, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 100 ms
Memory: 28.4 MB
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        n = len(height)

        maxar = 0

        # 2 PTR - left and right
        # move pointer whose height is less
        i = 0
        j = n-1
        while i<j:
            l = min(height[i], height[j])
            b = j-i
            ar = l*b

            maxar = max(ar,maxar)

            if height[i] < height[j]:
                i += 1
            else:
                j-=1
        
        return maxar

