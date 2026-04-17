"""
Problem Name: Merge Intervals
Difficulty: Medium
Tags: Array, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 8 ms
Memory: 20.9 MB
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Create a stack
        # Initially, put only first interval of given list into stack
        # Loop traversal from second interval onwards
        # if Stack not empty, pop top of stack.
        # Check if overlap
        # Create new interval to address overlap
        # Push new interval to stack again

        intervals.sort()
        #print(intervals)
        
        ret = []
        i = 0
        ret.append(intervals[0])

        for j in range(1, len(intervals)):
            
            if ret[-1][1] >= intervals[j][0]:
                temp = ret.pop()
                newInterval = [min(temp[0], intervals[j][0]), max(temp[1], intervals[j][1])]
                ret.append(newInterval)
            else:
                ret.append(intervals[j])
        
        print(ret)
        return ret

"""
Submission 2
Language: python3
Runtime: 13 ms
Memory: 20.8 MB
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Create a stack
        # Initially, put only first interval of given list into stack
        # Loop traversal from second interval onwards
        # if Stack not empty, pop top of stack.
        # Check if overlap
        # Create new interval to address overlap
        # Push new interval to stack again

        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        #print(intervals)
        
        ret = []
        i = 0
        ret.append(intervals[0])

        for j in range(1, len(intervals)):
            
            if ret[-1][1] >= intervals[j][0]:
                temp = ret.pop()
                newInterval = [min(temp[0], intervals[j][0]), max(temp[1], intervals[j][1])]
                ret.append(newInterval)
            else:
                ret.append(intervals[j])
        
        print(ret)
        return ret

