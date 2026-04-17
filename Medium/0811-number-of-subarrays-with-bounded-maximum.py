"""
Problem Name: Number of Subarrays with Bounded Maximum
Difficulty: Medium
Tags: Array, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 35 ms
Memory: 23.8 MB
"""
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # We're considering each and every subarray \
        # starting at every position
        
        # 2 Pointers for Sliding window
        lptr, rptr = 0, 0
        curlen = 0
        count = 0
        
        for rptr in range(len(nums)):
            if left <= nums[rptr] <= right:
                curlen = rptr - lptr + 1
            elif nums[rptr] > right:
                curlen = 0
                lptr = rptr + 1
            count += curlen
        
        return count

