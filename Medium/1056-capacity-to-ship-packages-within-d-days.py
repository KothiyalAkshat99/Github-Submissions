"""
Problem Name: Capacity To Ship Packages Within D Days
Difficulty: Medium
Tags: Array, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 183 ms
Memory: 22.2 MB
"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ret = r

        def daysTaken(minwt):
            numdays = 1
            curwt = 0
            for w in weights:
                if curwt + w > minwt:
                    numdays += 1
                    curwt = w
                else:
                    curwt += w
            return numdays
        
        while l <= r:
            m = (l + r) // 2
            numdays = daysTaken(m)

            if numdays > days:
                l = m + 1
            else:
                ret = m
                r = m - 1
        
        return ret
        

"""
Submission 2
Language: python3
Runtime: 179 ms
Memory: 23.8 MB
"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minwt = max(weights) # Min weight capacity
        maxwt = sum(weights) # Max weight capacity
        retCap = maxwt

        def calculateDaysTaken(capacity):
            daysTaken = 1
            s = 0
            for wt in weights:
                s += wt
                if s > capacity:
                    daysTaken += 1
                    s = wt

            return daysTaken

        while minwt <= maxwt:
            capacity = (minwt + maxwt) // 2
            daysTaken = calculateDaysTaken(capacity)

            if daysTaken > days:
                minwt = capacity + 1
            else:
                retCap = capacity
                maxwt = capacity - 1
        
        return retCap

