"""
Problem Name: Single Number
Difficulty: Easy
Tags: Array, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.5 MB
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # MAP - Non-constant space
        # Sorting - Non-linear runtime
        # XOR - A xor A is 0, A xor B is A/B if A=1/B=1
        # [2*(sum of range) - (sum of array)]
        x = 0
        for i in nums:
            x = x ^ i
        
        return x

"""
Submission 2
Language: python3
Runtime: 19 ms
Memory: 19.6 MB
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # MAP - Non-constant space
        # Sorting - Non-linear runtime
        # XOR - A xor A is 0, A xor B is A/B if A=1/B=1
        # [2*(sum of range) - (sum of array)]
        x = 0
        for i in nums:
            x = x ^ i
            print(x)
        
        return x

"""
Submission 3
Language: python3
Runtime: 6 ms
Memory: 19.6 MB
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        
        return res

