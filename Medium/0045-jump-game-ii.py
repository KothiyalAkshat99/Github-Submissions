"""
Problem Name: Jump Game II
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 7 ms
Memory: 18.8 MB
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        # GREEDY BFS

        ret = 0 # Counting number of jumps
        l = r = 0 # Window of jump, being considered for BFS

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                # Who can jump the farthest
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            ret += 1
        
        return ret

