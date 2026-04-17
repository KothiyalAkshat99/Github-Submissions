"""
Problem Name: First Bad Version
Difficulty: Easy
Tags: Binary Search, Interactive
"""

"""
Submission 1
Language: python3
Runtime: 38 ms
Memory: 17.9 MB
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if not n:
            return 0
        
        ret = -1

        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2
            isBad = isBadVersion(mid)

            if isBad:
                r = mid - 1
                ret = mid
            else:
                l = mid + 1
        
        return ret

