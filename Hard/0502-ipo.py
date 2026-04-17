"""
Problem Name: IPO
Difficulty: Hard
Tags: Array, Greedy, Sorting, Heap (Priority Queue)
"""

"""
Submission 1
Language: python3
Runtime: 402 ms
Memory: 44.9 MB
"""
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 2 HEAP Approach
        # 1 MINheap, 1 MAXheap
        # MINHEAP -> in order of min capital (capital, profit)
        # Get min cap <= w
        # Push this into MAXHEAP (profit) so we can get the max profit out of available projects.

        maxProfit = [] # Projects which we can afford
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush_max(maxProfit, p)

            if not maxProfit:
                break
            w += heapq.heappop_max(maxProfit)
        
        return w

