"""
Problem Name: Find the City With the Smallest Number of Neighbors at a Threshold Distance
Difficulty: Medium
Tags: Dynamic Programming, Graph Theory, Shortest Path
"""

"""
Submission 1
Language: python3
Runtime: 287 ms
Memory: 20.2 MB
"""
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # FLOYD - WARSHALL
        shortest_path = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            shortest_path[i][i] = 0     # Each node's distance to itself

        for u, v, wt in edges:
            shortest_path[u][v] = wt
            shortest_path[v][u] = wt
        
        # FLOYD-WARSHALL
        # Finds shortest path between ALL pairs of vertices in wtd graph
        # Handles negative weights
        # Unlike DIJKSTRA which handles only single source
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Update shortest path from i to j thru k
                    shortest_path[i][j] = min(
                        shortest_path[i][j],
                        shortest_path[i][k] + shortest_path[k][j],
                    )

        ret = -1    # City with fewest reachable
        ret_count = n

        for i in range(n):
            count = sum(
                1
                for j in range(n)
                if i != j and shortest_path[i][j] <= distanceThreshold
            )

            if count <= ret_count:
                ret_count = count
                ret = i

        return ret

"""
Submission 2
Language: python3
Runtime: 111 ms
Memory: 21 MB
"""
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # DIJKSTRA
        adj = {i:[] for i in range(n)}
        
        shortest_path = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            shortest_path[i][i] = 0     # Each node's distance to itself

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        
        # DJIKSTRA
        def dijkstra(src):
            minHeap = [(0, src)]
            shortest_path[src][:] = [float('inf')] * n
            shortest_path[src][src] = 0

            while minHeap:
                curr_dist, curr_node = heapq.heappop(minHeap)

                if curr_dist > shortest_path[src][curr_node]:
                    continue
                
                for nb, wt in adj[curr_node]:
                    if shortest_path[src][nb] > curr_dist + wt:
                        shortest_path[src][nb] = curr_dist + wt
                        heapq.heappush(minHeap, \
                            (shortest_path[src][nb], nb))
        
        
        # Shortest paths from each city using Dijkstra's
        for i in range(n):
            dijkstra(i)


        ### Find city with fewest number of reachable cities within thrsh
        ret = -1    # City with fewest reachable
        ret_count = n

        for i in range(n):
            count = sum(
                1
                for j in range(n)
                if i != j and shortest_path[i][j] <= distanceThreshold
            )

            if count <= ret_count:
                ret_count = count
                ret = i

        return ret

