"""
Problem Name: Lexicographically Minimum String After Removing Stars
Difficulty: Medium
Tags: Hash Table, String, Stack, Greedy, Heap (Priority Queue)
"""

"""
Submission 1
Language: python3
Runtime: 639 ms
Memory: 29.9 MB
"""
class Solution:
    def clearStars(self, s: str) -> str:
        # Keep track of index of smallest character while iterating thru loop
        # MinHeap?
        # Keep adding characters to minheap while iterating thru loop (character, -index)
        # If * found, remove maximum index of minimum character from minheap
        # (If only 1 occurence, pop directly)
        
        if not s: return ""

        n = len(s)
        minHeap = [] # MinHeap to store characters (character, -index)
        keep = [True] * n # To flag characters which need to be removed

        for i in range(n):
            x = s[i] # Character extraction
            if x != '*':
                heapq.heappush(minHeap, (x, -i)) # Stores character, latest index
            else:
                ch, neg = heapq.heappop(minHeap)
                keep[i] = False                 # Mark '*' for removal
                keep[-neg] = False               # Mark min character for removal
        
        return ''.join(s[i] for i in range(n) if keep[i])

