"""
Problem Name: Car Pooling
Difficulty: Medium
Tags: Array, Sorting, Heap (Priority Queue), Simulation, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.9 MB
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sorting trips by trip starting point (trip[1])
        trips.sort(key = lambda t: t[1])

        minHeap = []    # Keeps track of (endpos, Passengers)
        curPass = 0     # CUrrent num of passengers

        for trip in trips:
            numPass, start, end = trip

            # While previous trip of earliest drop time has start < current start
            # This means that minHeap[0] trip has been completed
            # We're checking this when we iterate over a new trip 
            while minHeap and minHeap[0][0] <= start:
                curPass -= minHeap[0][1]    # Since trip has been completed
                heapq.heappop(minHeap)      # Remove completed trip from heap
            
            curPass += numPass
            if curPass > capacity:     # If adding new passengers exceeds cap
                return False

            heapq.heappush(minHeap, (end, numPass))
        
        return True

