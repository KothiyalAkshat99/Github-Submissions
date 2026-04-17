"""
Problem Name: Length of the Longest Subsequence That Sums to Target
Difficulty: Medium
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 5974 ms
Memory: 91.9 MB
"""
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        INF = 10**20
        memo = [[None] * (target+1) for _ in range(n+1)]
        def dfs(i, pathsum):
            if pathsum == target:
                return 0
            if i == n:
                return -INF
            if pathsum > target:
                return -INF
            if memo[i][pathsum] is not None:
                return memo[i][pathsum]
            
            best = dfs(i+1, pathsum)
            best = max(best, dfs(i+1, pathsum + nums[i]) + 1)

            memo[i][pathsum] = best
            return best
        
        ret = dfs(0, 0)

        return ret if ret >= 0 else -1

"""
Submission 2
Language: python3
Runtime: 2051 ms
Memory: 17.9 MB
"""
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target+1)
        dp[0] = 0

        # Iterating thru nums
        for num in nums:
            # Iterating from target to nums
            for s in range(target, num-1, -1):
                if dp[s-num] != -1:
                    dp[s] = max(dp[s], dp[s-num] + 1)
        
        return dp[target]

