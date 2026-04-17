"""
Problem Name: Find in Mountain Array
Difficulty: Hard
Tags: Array, Binary Search, Interactive
"""

"""
Submission 1
Language: python3
Runtime: 47 ms
Memory: 20.1 MB
"""
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        l = 1
        r = n - 2
        peak = 0
        
        # Trying to find peak using Bin Search
        while l <= r:
            mid = (l + r) // 2
            x_prev = mountainArr.get(mid - 1)
            x_mid = mountainArr.get(mid)
            x_next = mountainArr.get(mid + 1)

            if x_prev < x_mid and x_mid > x_next:
                peak = mid
                break
            elif x_prev < x_mid < x_next:
                l = mid + 1
            elif x_prev > x_mid > x_next:
                r = mid - 1
        
        # Search left portion
        l = 0
        r = peak
        while l <= r:
            mid = (l + r) // 2
            x = mountainArr.get(mid)
            if x == target:
                return mid
            elif target > x:
                l = mid + 1
            elif target < x:
                r = mid - 1
        
        # Search right portion
        l = peak
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            x = mountainArr.get(mid)
            if x == target:
                return mid
            elif target > x:
                r = mid - 1
            elif target < x:
                l = mid + 1
            
        return -1

