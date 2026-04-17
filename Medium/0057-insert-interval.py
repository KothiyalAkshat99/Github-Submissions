"""
Problem Name: Insert Interval
Difficulty: Medium
Tags: Array
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.8 MB
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # inserting new interval [No Overlap]
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # [No Overlap currently]
                res.append(intervals[i])
            else: # Overlap case
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)

        return res

