"""
Problem Name: Course Schedule III
Difficulty: Hard
Tags: Array, Greedy, Sorting, Heap (Priority Queue)
"""

"""
Submission 1
Language: python3
Runtime: 37 ms
Memory: 23.2 MB
"""
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:      
        courses.sort(key = lambda x : x[1])
        currtime = 0
        maxheap = []    # Storing duration of courses taken

        for duration, deadline in courses:
            if currtime + duration <= deadline:     # Checking if we can take this course
                currtime += duration
                heapq.heappush_max(maxheap, duration)
            
            elif maxheap and maxheap[0] >= duration:      
                # Keeping track of LONGEST course taken yet
                # If current course duration is shorter than a previously taken LONG course,
                # We swap it out
                currtime += duration - heapq.heappop_max(maxheap)
                heapq.heappush_max(maxheap, duration)
        
        return len(maxheap)

