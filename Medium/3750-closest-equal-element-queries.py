"""
Problem Name: Closest Equal Element Queries
Difficulty: Medium
Tags: Array, Hash Table, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 366 ms
Memory: 54.1 MB
"""
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        hashmap = {}
        n = len(nums)
        left = [0] * n      # Nearest index to LEFT of i with same val
        right = [0] * n     # Nearest index to RIGHT of i with same val

        # First Pass -> L to R
        for i in range(-n, n):
            if i >= 0:
                left[i] = hashmap.get(nums[i], -n)
            hashmap[nums[(i + n) % n]] = i
        
        hashmap.clear()

        # Second Pass -> R to L
        for i in range(2 * n - 1, -1, -1):
            if i < n:
                right[i] = hashmap.get(nums[i], 2 * n)
            hashmap[nums[i % n]] = i
        
        ret = []
        for query in queries:
            if query - left[query] == n:
                ret.append(-1)
            else:
                ret.append(min(query - left[query], right[query] - query))
        
        return ret

