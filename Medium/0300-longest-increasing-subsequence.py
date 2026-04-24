"""
Problem Name: Longest Increasing Subsequence
Difficulty: Medium
Tags: Array, Binary Search, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 1821 ms
Memory: 18 MB
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums), -1, -1): # Last to first
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

"""
Submission 2
Language: python3
Runtime: 1037 ms
Memory: 19.4 MB
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n    # dp[i] = longest subsequence of nums[0..i]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        
        return max(dp)

