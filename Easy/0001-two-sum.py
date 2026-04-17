"""
Problem Name: Two Sum
Difficulty: Easy
Tags: Array, Hash Table
"""

"""
Submission 1
Language: python3
Runtime: 54 ms
Memory: 17.5 MB
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in map:
                return [i, map[y]]
            map[x] = i

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 18.9 MB
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in hmap:
                return [i, hmap[y]]
            hmap[x] = i

