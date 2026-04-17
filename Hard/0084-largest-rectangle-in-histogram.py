"""
Problem Name: Largest Rectangle in Histogram
Difficulty: Hard
Tags: Array, Stack, Monotonic Stack
"""

"""
Submission 1
Language: python3
Runtime: 162 ms
Memory: 35.8 MB
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic Stack
        # Increasing monotonic
        # While new height is lower than stack top, check what stack top
        # - contributed to the max area
        # Pop it

        # Keep [Start index, height] in Stack 
        # Start index is NOT the index where that height is found
        # Instead, it is the point till where we can extend that -
        # - particular height, going backwards.

        maxAr = 0
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start = i
            # If new incoming height is smaller, older TALLER heights - 
            # cannot be extended anymore.
            # So popping at that point, and checking the AREA contribution
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                maxAr = max(maxAr, height * width)
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxAr = max(maxAr, h * (len(heights) - i))
        
        return maxAr

