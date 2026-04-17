"""
Problem Name: Network Delay Time
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path
"""

"""
Submission 1
Language: python3
Runtime: 1969 ms
Memory: 22 MB
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}   # Adjacency List -> {source:[(target, time)]}
        time = [float('inf')] * (n + 1) # Time to reach each node

        for u, v, w in times:
            if u not in adj:
                adj[u] = []
            adj[u].append((v, w))
        
        def dfs(node, node_time):
            if not adj[node]:
                return
            
            for nb, tm in adj[node]:
                arrival_time = node_time + tm
                
                # Pruning 
                # Only traverse if we're improving on time.
                if arrival_time < time[nb]:
                    time[nb] = arrival_time
                    dfs(nb, time[nb])


        time[k] = 0
        dfs(k, 0)

        time = time[1:]     # Ignoring index 0
        max_time = max(time)
        
        return max_time if max_time != float('inf') else -1

"""
Submission 2
Language: python3
Runtime: 356 ms
Memory: 21.3 MB
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ### DIJKSTRA - Shortest Path -> BFS + MinHeap
        
        adj = {i:[] for i in range(1, n + 1)}   # Adjacency List -> {source:[(target, time)]}

        for u, v, w in times:
            if u not in adj:
                adj[u] = []
            adj[u].append((v, w))
        
        # MinHeap used to process closest nodes first
        # Guarantees that the first time you visit a node, that is shortest path.
        minHeap = [(0, k)]  # Initialize MinHeap with starting Node (currtime, currnode)
        visited = set()
        max_time = 0

        while minHeap:
            curr_time, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            
            visited.add(node)
            max_time = max(max_time, curr_time)

            for nb, tm in adj[node]:
                if nb not in visited:
                    heapq.heappush(minHeap, (curr_time + tm, nb))
        
        return max_time if len(visited) == n else -1

