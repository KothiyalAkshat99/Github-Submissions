"""
Problem Name: Divisible and Non-divisible Sums Difference
Difficulty: Easy
Tags: Math
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.9 MB
"""
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = (n * (n + 1)) // 2

        k = n // m
        divsum = m * ((k * (k + 1)) // 2)

        nondiv = total - divsum

        return nondiv - divsum
        

"""
Submission 2
Language: python3
Runtime: 2 ms
Memory: 17.6 MB
"""
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1, nums2 = 0, 0
        for i in range(1,n+1):
            if i % m == 0:
                nums2 += i
            else:
                nums1 += i
        
        return nums1 - nums2

