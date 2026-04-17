"""
Problem Name: Non-overlapping Intervals
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 171 ms
Memory: 51.4 MB
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 1:
            return 0
        
        intervals.sort()
        
        ret = 0
        prevEnd = intervals[0][1]

        # While comparing intervals, in case of overlaps - 
        # Delete intervals which has higher end value.
        # This way, interval with lower end value is left, and has LESS chance of overlaps

        for start, end in intervals[1:]:
            # No Overlap:
            if start >= prevEnd:
                prevEnd = end
            # Handling Overlap case:
            else:
                ret += 1    # Tracking number of deletions
                prevEnd = min(end, prevEnd) # Not deleting but just updating
        
        return ret

