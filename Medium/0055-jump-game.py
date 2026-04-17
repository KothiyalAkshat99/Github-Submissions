"""
Problem Name: Jump Game
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 18.7 MB
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False

"""
Submission 2
Language: python3
Runtime: 10 ms
Memory: 18.8 MB
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True
        
        n = len(nums)
        goal = n-1
        for i in range(n-2, -1, -1):
            if goal <= i + nums[i]:
                goal = i
        
        if goal != 0:
            return False
        
        return True

"""
Submission 3
Language: python3
Runtime: 44 ms
Memory: 18.4 MB
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        reach = 0 # initially

        for i in range(len(nums)):
            if reach < i:
                return False
            
            reach = max(reach, i + nums[i])
            i += 1
        
        return True

