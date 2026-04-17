"""
Problem Name: Minimum Interval to Include Each Query
Difficulty: Hard
Tags: Array, Binary Search, Sweep Line, Sorting, Heap (Priority Queue)
"""

"""
Submission 1
Language: python3
Runtime: 259 ms
Memory: 59 MB
"""
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Min heap + hashmap?
        # Hashmap -> keys = interval length, values = [intervals]

        if not intervals or not queries: return -1

        # If we sort both lists, chances of particular query solutions to fall in order are higher
        
        intervals.sort()

        minHeap = []

        ret = {}
        i = 0 # index for intervals traversal

        # We'll be building a minHeap for each query

        # We'll add only those intervals to minHeap where a query might exist
        # If interval[start] > query, NOT added to minHeap

        # MinHeap nodes are in the form [size, interval[right]]
        # Tiebreaker in case of equal size = interval[right]
        # Min interval in this case = one with LOWER interval[right]

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                # In above condition, we're only checking intervals where start <= query
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and q > minHeap[0][1]:
                heapq.heappop(minHeap)
            
            ret[q] = minHeap[0][0] if minHeap else -1
        
        return [ret[q] for q in queries]

