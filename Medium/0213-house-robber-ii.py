"""
Problem Name: House Robber II
Difficulty: Medium
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_max(nums):
            prev_rob = max_rob = 0

            for cur in nums:
                temp = max(max_rob, prev_rob + cur)
                prev_rob = max_rob
                max_rob = temp
            
            return max_rob
        # Either we take first and not last
        # OR last and not first
        # OR only first in case of only 1 house.
        return max(get_max(nums[:-1]), get_max(nums[1:]), nums[0])


"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19.4 MB
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def outer(arr):
            memo = {}

            # Instead of passing arr into recur directly,
            # we pass it to an outer function.
            # Outer also helps with creating separate memo caches
            def recur(i):
                if i >= len(arr):
                    return 0
                
                if i in memo:
                    return memo[i]
                
                # Rob or skip
                ret = max(arr[i] + recur(i + 2), recur(i + 1))
                memo[i] = ret

                return memo[i]
            
            return recur(0)
        
        # 2 cases
        # 1. Skip last home
        # 2. Skip first home
        # Select max of these 2 routes.
        return max(outer(nums[:-1]), outer(nums[1:]))

