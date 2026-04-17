"""
Problem Name: Contains Duplicate
Difficulty: Easy
Tags: Array, Hash Table, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 415 ms
Memory: 34.5 MB
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numdict = {}
        for i in nums:
            if i in numdict:
                return True
            else:
                numdict[i] = 1
        
        return False

"""
Submission 2
Language: python3
Runtime: 13 ms
Memory: 31.5 MB
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

