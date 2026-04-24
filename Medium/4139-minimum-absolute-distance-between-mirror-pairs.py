"""
Problem Name: Minimum Absolute Distance Between Mirror Pairs
Difficulty: Medium
Tags: Array, Hash Table, Math
"""

"""
Submission 1
Language: python3
Runtime: 298 ms
Memory: 42 MB
"""
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # hashmap[v] = most recent index (j) s.t. \
        # reverse(nums[j]) = v
        hashmap = {}
        min_dist = len(nums)

        def reverseNumber(num: int) -> int:
            temp = 0
            while num:
                temp = temp * 10 + num % 10
                num = num // 10
            return temp

        for i, num in enumerate(nums):
            num_reverse = reverseNumber(num)
            # If num in hashmap, \
            # means that there is a previous index j \
            # s.t. reverse(nums[j]) = num
            # (j, i) then forms a pair and we can update with (i - j)

            # Thus we compute reverse(num) and set hmap[reverse] = i\
            # Indicates current index can form a pair with future elements\
            # whose value equals reverse(num)

            # We keep most recent index always
            if num in hashmap:
                min_dist = min(min_dist, i - hashmap[num])
            
            hashmap[num_reverse] = i
        
        return -1 if min_dist == len(nums) else min_dist

