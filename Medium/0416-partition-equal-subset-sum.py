"""
Problem Name: Partition Equal Subset Sum
Difficulty: Medium
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 428 ms
Memory: 17.9 MB
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total //2 

        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for i in range(len(dp) -1, n-1, -1):
                if dp[i]:continue
                if dp[i-n]:dp[i] = True
                if dp[-1]:return True
        
        return False

"""
Submission 2
Language: python3
Runtime: 680 ms
Memory: 160.6 MB
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        total_sum = sum(nums)
        if total_sum % 2 != 0:  # Odd total sum cannot be partitioned
            return False
        
        n = len(nums)
        memo = {}

        target_sum = total_sum // 2     # Target per partition
        
        # Since we have total_sum, we only need to track 1 half of the partition
        def recur(i: int, curr_sum: int) -> bool:
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            if curr_sum == target_sum:
                return True
            
            if i >= n or curr_sum > target_sum:
                return False
            
            ret = recur(i + 1, curr_sum + nums[i]) or \
                  recur(i + 1, curr_sum)
            
            memo[(i, curr_sum)] = ret
            return ret
        
        return recur(0, 0)

