"""
Problem Name: Second Minimum Time to Reach Destination
Difficulty: Hard
Tags: Breadth-First Search, Graph Theory, Shortest Path
"""

"""
Submission 1
Language: python3
Runtime: 603 ms
Memory: 33.1 MB
"""
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = {i:set() for i in range(1, n + 1)}

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        # Weight per edge == time == 3, constant for all edges
        
        dist1 = {i: float('inf') for i in range(1, n + 1)}  # Min dist from node 1 to all nodes
        dist2 = {i: float('inf') for i in range(1, n + 1)}  # SECOND min dist from node 1

        # Num times a node is popped out of queue
        # Since we need second min, each node can be popped out at-most twice
        freq = [0] * (n + 1)

        pq = [(0, 1)]
        dist1[1] = 0

        while pq:
            timeTaken, node = heapq.heappop(pq)
            freq[node] += 1

            if freq[node] == 2 and node == n:
                return timeTaken
            
            if (timeTaken // change) % 2:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken = timeTaken + time
            
            for nb in adj[node]:
                if freq[nb] == 2:
                    continue
                
                if dist1[nb] > timeTaken:
                    dist2[nb] = dist1[nb]
                    dist1[nb] = timeTaken
                    heapq.heappush(pq, (timeTaken, nb))
                
                elif dist2[nb] > timeTaken and dist1[nb] != timeTaken:
                    dist2[nb] = timeTaken
                    heapq.heappush(pq, (timeTaken, nb))
        
        return 0

