"""
Problem Name: Next Greater Element I
Difficulty: Easy
Tags: Array, Hash Table, Stack, Monotonic Stack
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18 MB
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Monotonic Stack - Decreasing in this case

        # Iterate thru nums2
        # Add number to stack if it is not > any number on stack, OR if it is in nums1
        # If current number is greater than current top, pop current top and set value in result
        # Keep on doing this until current number > stack top

        stk = []
        nums1idx = {n:i for i, n in enumerate(nums1)} # number:index hashmap
        ret = [-1] * len(nums1)

        for i in range(len(nums2)):
            cur = nums2[i]
            while stk and cur > stk[-1]:
                val = stk.pop()
                ret[nums1idx[val]] = cur
            if cur in nums1idx:
                stk.append(cur)
        
        return ret

