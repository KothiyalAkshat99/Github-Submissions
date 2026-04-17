"""
Problem Name: Reorganize String
Difficulty: Medium
Tags: Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting
"""

"""
Submission 1
Language: python3
Runtime: 2 ms
Memory: 18 MB
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        # HashMap + MaxHeap
        # We get the most frequent character first. Put it in result
        # Now this character goes on HOLD
        # WE get NEXT frequent character
        # Now we can use the initial ONHOLD character

        count = Counter(s) # Hashmap {char:count}
        maxHeap = [(-c, char) for char, c in count.items()] # Maxheap based on Frequency
        heapq.heapify(maxHeap) # O(n)

        prev = None
        ret = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            # Need most frequent character except prev
            c, char = heapq.heappop(maxHeap)
            ret += char
            c += 1 # Decrementing -count

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if c != 0:
                prev = (c, char)
        
        return ret

"""
Submission 2
Language: python3
Runtime: 4 ms
Memory: 19.6 MB
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(freq, char) for char, freq in count.items()]
        heapq.heapify_max(maxHeap)  # Heapify is a O(n) operation unlike heappush, heappop

        heldChar = None
        ret = ""

        while maxHeap or heldChar:
            # This happens when only 1 element left with freq > 1
            # Failure case. No other characters can be substituted in between.
            if heldChar and not maxHeap: 
                return ""
            
            freq, char = heapq.heappop_max(maxHeap)  # Get (freq, char) for max freq character
            freq -= 1
            
            ret += char
            
            # Re-insert previous held-out Character into maxHeap
            if heldChar:
                heapq.heappush_max(maxHeap, heldChar)
                heldChar = None
            
            # If current character has count left, put it on hold
            if freq != 0:
                heldChar = (freq, char)
                
        return ret

