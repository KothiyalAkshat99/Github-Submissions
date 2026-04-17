"""
Problem Name: Maximize Distance to Closest Person
Difficulty: Medium
Tags: Array
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 18.2 MB
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if not seats:
            return 0
        # Seat can be in between 2 other people, or can be within [0 - 1] or [1-EOL]

        prev = -1 # Tracks index where last seat found
        ret = 0

        for i in range(len(seats)):
            if seats[i]:
                if prev == -1:
                    ret = max(ret, i)
                else:
                    ret = max(ret, (i-prev) // 2)
                prev = i
        
        ret = max(ret, len(seats) - 1 - prev) # In case max distance at last leg of list
        return ret

