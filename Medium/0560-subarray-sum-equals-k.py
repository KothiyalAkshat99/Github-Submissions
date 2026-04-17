"""
Problem Name: Subarray Sum Equals K
Difficulty: Medium
Tags: Array, Hash Table, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 23 ms
Memory: 20.2 MB
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, cursum = 0, 0

        hmap = {0:1}

        for i in range(len(nums)):
            cursum += nums[i]

            if (cursum-k) in hmap:
                count += hmap[cursum-k]
            
            hmap[cursum] = 1 + hmap.get(cursum, 0)
        
        return count


