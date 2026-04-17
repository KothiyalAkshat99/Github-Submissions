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

