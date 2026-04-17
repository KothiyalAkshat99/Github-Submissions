"""
Problem Name: Minimum Equal Sum of Two Arrays After Replacing Zeros
Difficulty: Medium
Tags: Array, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 935 ms
Memory: 34.8 MB
"""
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        def countSum(nums):
            nz, nsum = 0, 0
            for i in nums:
                nsum += i
                if not i:
                    nz += 1
                    nsum += 1 # Essentially replacing all of the 0's with 1's
                
            return nz, nsum
        
        n1z, n1sum = countSum(nums1)
        n2z, n2sum = countSum(nums2)

        if (n1z == 0 and n2sum > n1sum) or (n2z == 0 and n1sum > n2sum):
            return -1
        
        return max(n1sum, n2sum)

