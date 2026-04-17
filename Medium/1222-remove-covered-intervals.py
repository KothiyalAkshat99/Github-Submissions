"""
Problem Name: Remove Covered Intervals
Difficulty: Medium
Tags: Array, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 1 ms
Memory: 18.1 MB
"""
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: (i[0], -i[1])) # ASC interval start, DESC interval end

        res = [intervals[0]]

        for l, r in intervals[1:]:
            prevL, prevR = res[-1]

            if prevL <= l and prevR >= r:
                continue
            
            res.append([l, r])

        return len(res)

