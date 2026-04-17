"""
Problem Name: Minimum Size Subarray Sum
Difficulty: Medium
Tags: Array, Binary Search, Sliding Window, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 28.4 MB
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Move a sliding window over the array
        # When cursum < target -> move right forward
        # When cursum >= target -> update minlen
        # At this point, move left forward till the point cursum >= target
        # Keep updating minlen if necessary

        left, right = 0, 0
        minlen = len(nums) + 1
        cursum = 0

        while right < len(nums):
            cursum += nums[right]

            while cursum >= target:
                minlen = min(minlen, right - left + 1)
                cursum -= nums[left]
                left += 1
            right += 1
        
        return minlen if minlen != len(nums) + 1 else 0

