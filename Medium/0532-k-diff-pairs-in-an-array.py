"""
Problem Name: K-diff Pairs in an Array
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, Binary Search, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 19.2 MB
"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hmap = Counter(nums)
        count = 0

        for num in hmap:
            if k == 0:
                if hmap[num] >= 2:
                    count += 1
            else:
                if num + k in hmap:
                    count += 1
        return count

