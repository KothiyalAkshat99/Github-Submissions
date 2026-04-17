"""
Problem Name: Longest Happy String
Difficulty: Medium
Tags: String, Greedy, Heap (Priority Queue)
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.6 MB
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a:
            maxHeap.append((a, 'a'))
        if b:
            maxHeap.append((b, 'b'))
        if c:
            maxHeap.append((c, 'c'))
        heapq.heapify_max(maxHeap)

        ret = []

        while maxHeap:
            count, char = heapq.heappop_max(maxHeap)

            # If condition is about to be broken
            if len(ret) >= 2 and ret[-1] == char and ret [-2] == char:
                if not maxHeap:
                    break
                
                # Popping next frequent character
                count2, char2 = heapq.heappop_max(maxHeap)
                ret.append(char2)

                if count2-1 > 0:  # If this character has count left
                    heapq.heappush_max(maxHeap, (count2 - 1, char2))
                
                # Pushing first character back into heap
                heapq.heappush_max(maxHeap, (count, char))
            
            else:
                ret.append(char)
                if count-1 > 0:
                    heapq.heappush_max(maxHeap, (count - 1, char))
        
        return ''.join(ret)

