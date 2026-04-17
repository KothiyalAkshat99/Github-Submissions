"""
Problem Name: Maximum Erasure Value
Difficulty: Medium
Tags: Array, Hash Table, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 195 ms
Memory: 28.9 MB
"""
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxsum = 0
        l = 0
        hset = set()
        cursum = 0

        for r in range(len(nums)):
            while nums[r] in hset:
                cursum -= nums[l]
                hset.remove(nums[l])
                l += 1
            hset.add(nums[r])
            cursum += nums[r]
            maxsum = max(cursum, maxsum)
        
        return maxsum

