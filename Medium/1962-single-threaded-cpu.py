"""
Problem Name: Single-Threaded CPU
Difficulty: Medium
Tags: Array, Sorting, Heap (Priority Queue)
"""

"""
Submission 1
Language: python3
Runtime: 195 ms
Memory: 66 MB
"""
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ret = []

        tasks = sorted([(t[0], t[1], i) for i,t in enumerate(tasks)])

        minHeap = []
        time = 0

        for task in tasks:
            while minHeap and task[0] > time:
                poppedTask = heapq.heappop(minHeap)
                ret.append(poppedTask[1])
                time += poppedTask[0]
            
            time = max(time, task[0])
            heapq.heappush(minHeap, (task[1], task[2]))
        
        return ret + [i for _, i in sorted(minHeap)]

