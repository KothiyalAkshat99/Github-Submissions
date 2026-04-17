"""
Problem Name: Last Stone Weight
Difficulty: Easy
Tags: Array, Heap (Priority Queue)
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        # Negating all values in the list to accomodate for MaxHeap
        stones = [-i for i in stones]
        
        # Since heapify by default is minHeap implemented
        heapq.heapify(stones)

        ret = 0

        while True:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            t = x - y
            if abs(t) != 0:
                heapq.heappush(stones, -t)
            if not stones:
                ret = 0
                break
            if len(stones) == 1:
                ret = -stones[0]
                break
        
        return ret

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19.5 MB
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) != 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            heapq.heappush_max(stones, abs(x-y))
        
        return stones[0]

