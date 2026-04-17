"""
Problem Name: Split Array Largest Sum
Difficulty: Hard
Tags: Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.2 MB
"""
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # We'll do a binary search over a range
        # Range = [max(nums), sum(nums)]
        # We'll check if the taken value using bin search
            # can be taken as max subarray sum or no
            # If yes, move to smaller side
            # If no, move to larger side
        
        # Helper function
        def canSplit(largest):
            count = 0 # Count of possible subarrays
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    count += 1
                    curSum = n
            
            return count + 1 <= k
        

        l = max(nums)
        r = sum(nums)
        ret = r

        while l <= r:
            # Calculates mid as usual, just prevents overflow
            # Same as (l + r) // 2
            mid = l + ((r - l) // 2) 

            if canSplit(mid):
                ret = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ret

