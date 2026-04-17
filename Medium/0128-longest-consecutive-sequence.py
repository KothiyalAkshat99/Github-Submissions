"""
Problem Name: Longest Consecutive Sequence
Difficulty: Medium
Tags: Array, Hash Table, Union-Find
"""

"""
Submission 1
Language: python3
Runtime: 323 ms
Memory: 31.8 MB
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        l = 0

        for i in nums:
            if (i-1) not in nums:
                j = i
                strk = 1

                while True:
                    if j+1 in nums:
                        j += 1
                        strk += 1
                    else:
                        break
                
                if strk>l:
                    l = strk
            
        return l

"""
Submission 2
Language: python3
Runtime: 39 ms
Memory: 34.2 MB
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ret = 0

        for n in nums_set:
            if n-1 not in nums_set:
                length = 1
                
                while n + length in nums_set:
                    length += 1
                
                ret = max(ret, length)
        
        return ret

