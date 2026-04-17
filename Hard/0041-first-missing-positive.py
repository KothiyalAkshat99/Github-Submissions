"""
Problem Name: First Missing Positive
Difficulty: Hard
Tags: Array, Hash Table
"""

"""
Submission 1
Language: python3
Runtime: 75 ms
Memory: 28.7 MB
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # since we don't need -ve values, change all to 0
        # We'll use input array as extra memory here.
        # Instead of a hashmap, indices will be used as keys.
        # Whatever values we've found, we'll mark respective indices as -ve.
        # Showing that we have those values in hand.
        # Hence accessing index is gonna tell us if we've found a value before.

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                # If we've not found that value yet (index still +ve)
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return len(nums) + 1

