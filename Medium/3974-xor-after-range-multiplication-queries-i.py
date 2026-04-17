"""
Problem Name: XOR After Range Multiplication Queries I
Difficulty: Medium
Tags: Array, Divide and Conquer, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 1716 ms
Memory: 20 MB
"""
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            idx = l
            if idx > len(nums):
                continue
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (10 ** 9 + 7)
                idx += k
            
        ret = nums[0]
        for j in range(1, len(nums)):
            ret = ret ^ nums[j]
        
        return ret

