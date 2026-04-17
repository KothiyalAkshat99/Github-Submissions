"""
Problem Name: Min Cost to Connect All Points
Difficulty: Medium
Tags: Array, Union-Find, Graph Theory, Minimum Spanning Tree
"""

"""
Submission 1
Language: python3
Runtime: 561 ms
Memory: 23.5 MB
"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ### PRIM'S ALGO
        # Calculate distance between each pair of points
        # Start from initial point, mark as visited, select point with LEAST DIST among unvisited
        # Calculate distances from selected point to unvisited points, store in CACHE (distances)
        # Add min cost edge to Priority Queue using distances from cache
        # Repeat until all points visited and calculate min cost

        distances = {0:0}  # {Point: dist}
        minCost = 0
        visited = set()
        dq = [(0, 0)]   # (cost, vertex)

        while dq:
            cost, u = heapq.heappop(dq)

            if u in visited:
                continue
            
            visited.add(u)
            minCost += cost

            for v in range(len(points)):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < distances.get(v, float('inf')):
                        distances[v] = dist
                        heapq.heappush(dq, (dist, v))
        
        return minCost

"""
Submission 2
Language: python3
Runtime: 577 ms
Memory: 23.3 MB
"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ### PRIM'S ALGO
        # Calculate distance between each pair of points
        # Start from initial point, mark as visited, select point with LEAST DIST among unvisited
        # Calculate distances from selected point to unvisited points, store in CACHE (distances)
        # Add min cost edge to Priority Queue using distances from cache
        # Repeat until all points visited and calculate min cost

        # Distances here stores closest (relative) distance to each vertex?
        distances = {0:0}  # {Point: dist}
        minCost = 0
        visited = set()
        dq = [(0, 0)]   # (cost, vertex)

        while dq:   # We're only moving to next closest point (guaranteed)
            cost, u = heapq.heappop(dq)

            if u in visited:
                continue
            
            visited.add(u)
            minCost += cost

            for v in range(len(points)):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < distances.get(v, float('inf')):
                        distances[v] = dist
                        heapq.heappush(dq, (dist, v))
        
        return minCost

