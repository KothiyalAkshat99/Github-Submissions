"""
Problem Name: Trapping Rain Water
Difficulty: Hard
Tags: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
"""

"""
Submission 1
Language: python3
Runtime: 8 ms
Memory: 19.2 MB
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        # water at each pos = min(max left height, max right height) - height[i]

        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        ret = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                ret += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                ret += rightMax - height[r]
        
        return ret

"""
Submission 2
Language: python3
Runtime: 31 ms
Memory: 19.3 MB
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        # water at each pos = min(max left height, max right height) - height[i]
        
        if not height: return 0
        n = len(height)
        
        # For each index, storing Max height to left and right in respective arrays
        leftMax, rightMax = [0] * n, [0] * n
        
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        rightMax[n-1] = height[n-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        ret = 0
        # Calculating Trapped Water:
        # Water at each block = min(leftMax - rightMax) - height at current block
        for i in range(n):
            ret += min(leftMax[i], rightMax[i]) - height[i]
        
        return ret

