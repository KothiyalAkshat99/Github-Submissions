"""
Problem Name: Kth Largest Element in an Array
Difficulty: Medium
Tags: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
"""

"""
Submission 1
Language: python3
Runtime: 89 ms
Memory: 29.1 MB
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        ret = 0
        while k > 0:
            ret = heapq.heappop_max(nums)
            k -= 1
        
        return ret

