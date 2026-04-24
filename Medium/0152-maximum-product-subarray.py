"""
Problem Name: Maximum Product Subarray
Difficulty: Medium
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 18.5 MB
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = 1
        minprod = 1
        ret = max(nums)

        for n in nums:
            # Using minprod in case it is -ve \
            # and another -ve makes it > max +ve
            temp = maxprod * n
            maxprod = max(temp, minprod * n, n)
            minprod = min(temp, minprod * n, n)

            ret = max(ret, maxprod)
        
        return ret

"""
Submission 2
Language: python3
Runtime: 6 ms
Memory: 19.7 MB
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane -> Should I start a fresh array at any pos, or should I extend 
        if len(nums) == 1:
            return nums[0]
        
        max_prod, min_prod = 1, 1
        ret = 0

        for num in nums:
            # If we hit a 0, it essentially resets the product streak to 0
            
            # Temporary storage because curMax changes before curMin is calculated
            temp = max_prod * num
            
            # Three-way comparison: 
            # 1. New product with curMax
            # 2. New product with curMin (handles negative * negative)
            # 3. Just the current number (starts a fresh subarray)
            max_prod = max(num * max_prod, num * min_prod, num)
            min_prod = min(temp, num * min_prod, num)
            
            ret = max(ret, max_prod)
            
        return ret

"""
Submission 3
Language: python3
Runtime: 3 ms
Memory: 19.7 MB
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane -> Should I start a fresh array at any pos, or should I extend 
        if len(nums) == 1:
            return nums[0]
        
        max_prod, min_prod = 1, 1
        ret = 0

        for num in nums:
            # If current num is negative, 
            # We know that our max will become min (-ve),
            # And min might become max (+ve)
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            
            ret = max(ret, max_prod)
            
        return ret

