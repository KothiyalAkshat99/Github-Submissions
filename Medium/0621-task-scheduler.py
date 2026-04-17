"""
Problem Name: Task Scheduler
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting
"""

"""
Submission 1
Language: python3
Runtime: 142 ms
Memory: 19 MB
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time

        count = Counter(tasks) # Dictionary to count Frequencies
        maxHeap = [-c for c in count.values()] # Creating a maxheap using frequency counts only
        heapq.heapify(maxHeap)

        time = 0 # global time counter
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1
            
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap)
                if c: # if count becomes 0, can ignore
                    q.append([c, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
                

"""
Submission 2
Language: python3
Runtime: 170 ms
Memory: 21 MB
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = dict(Counter(tasks))
        # Create a Frequency/Count based maxheap
        # Why?
        # We are not concerned with WHICH job is being performed as such (Since we only need TOTAL TIME)
        # We are only keeping track of remaining frequency and idletime

        # Maxheap is the available pool -> Tasks which can be done currently
        maxHeap = [c for c in count.values()]
        heapq.heapify_max(maxHeap)

        time = 0 # Global timer 

        # Deque holds those jobs which are in downtime and cannot be performed.
        # It is kind of like a WAITING room

        # Using a deque here because it respects the order of insertion.
        # If the first task is on hold, the following tasks in queue will also be on hold.
        dq = deque() # Holds [freq, idleTime] pair

        while maxHeap or dq:
            time += 1

            if maxHeap:
                # Get maximum frequency count from Heap, decrease it by 1 (task completed)
                c = heapq.heappop_max(maxHeap) - 1
                # If remaining task freq != 0
                if c:
                    dq.append([c, time + n]) # Add [Count, currenttime + n] to deque
            
            # If the first element in deque has 
            if dq and dq[0][1] == time:
                heapq.heappush_max(maxHeap, dq.popleft()[0])
        
        return time

