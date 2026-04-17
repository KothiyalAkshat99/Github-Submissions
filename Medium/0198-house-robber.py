"""
Problem Name: House Robber
Difficulty: Medium
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18 MB
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        '''
        2 routes at each house -
        (A) Loot current house i - In this case, can't rob previous (i-1th) house, but can 
            proceed to loot i-2 and following.
            Current + loot from houses before previous
        (B) DO NOT loot current house i - Robber gets money from robbery of i-1 and all 
            following.
            Loot from previous + loot from before that
        '''
        memo = {}
        n = len(nums)

        def recur(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + recur(i-2), recur(i-1))
            # value = max(Loot current house, Skip current house)
            return memo[i]
        
        return recur(n-1)

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(1, n):
            val = nums[i]
            dp[i+1] = max(dp[i], dp[i-1] + val)
        
        return dp[n]

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 17.5 MB
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        n1 = 0
        n2 = 0

        for i in range(0, n):
            temp = n1
            n1 = max(n2 + nums[i], n1)
            n2 = temp
        
        return n1

"""
Submission 4
Language: python3
Runtime: 0 ms
Memory: 19.4 MB
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        memo = {}

        def recur(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            # Either we loot current hours (nums[i] + recur(i + 2))
            # Or we skip current and move to next house
            # We take max of these 2 at each step
            ret = max(nums[i] + recur(i + 2), recur(i + 1))
            memo[i] = ret

            return ret
        
        return recur(0)

"""
Submission 5
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        memo = {}
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(1, len(nums)):
            ret = max(nums[i] + memo[i - 1], memo[i])
            memo[i + 1] = ret
        
        return memo[len(nums)]

