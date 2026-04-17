"""
Problem Name: Peak Index in a Mountain Array
Difficulty: Medium
Tags: Array, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 29.6 MB
"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1

        while l<r:
            k = (l + r) // 2
            if arr[k+1] > arr[k]:
                l = k + 1
            else:
                r = k
        
        return l
        

