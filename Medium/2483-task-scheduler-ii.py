"""
Problem Name: Task Scheduler II
Difficulty: Medium
Tags: Array, Hash Table, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 89 ms
Memory: 36.8 MB
"""
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        hmap = {} # We track the task and their spacing in the hashmap
        count = 0

        for i in range(len(tasks)):
            task = tasks[i]
            count += 1

            if task in hmap and count < hmap[task]:
                count = hmap[task]
            hmap[task] = count + space + 1
        
        return count

