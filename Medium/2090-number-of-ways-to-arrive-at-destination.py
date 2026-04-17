"""
Problem Name: Number of Ways to Arrive at Destination
Difficulty: Medium
Tags: Dynamic Programming, Graph Theory, Topological Sort, Shortest Path
"""

"""
Submission 1
Language: python3
Runtime: 16 ms
Memory: 26.5 MB
"""
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        adj = {i:set() for i in range(n)}
        for u, v, time in roads:
            adj[u].add((v, time))
            adj[v].add((u, time))
        
        min_time = [float('inf')] * n
        min_heap = [(0, 0)]  # Priority Queue (time, node) -> Starting from node 0
        path_count = [0] * n    # Num Ways to reach each node in shortest time

        min_time[0] = 0     # Distance to Source
        path_count[0] = 1   # 1 way to reach node 0

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)

            if curr_time > min_time[curr_node]:
                continue
            
            for nb, time in adj[curr_node]:
                # Found a new shortest path
                if curr_time + time < min_time[nb]:
                    min_time[nb] = curr_time + time
                    path_count[nb] = path_count[curr_node]
                    heapq.heappush(min_heap, (min_time[nb], nb))
                
                # Found another way with same shortest path
                elif curr_time + time == min_time[nb]:
                    path_count[nb] = (path_count[nb] + path_count[curr_node]) % MOD
        
        return path_count[n-1]

