"""
Problem Name: Path with Maximum Probability
Difficulty: Medium
Tags: Array, Graph Theory, Heap (Priority Queue), Shortest Path
"""

"""
Submission 1
Language: python3
Runtime: 71 ms
Memory: 30.2 MB
"""
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # We'll record highest probab of reaching each node at each level
        adj = defaultdict(list)
        probab_cache = [0.0] * n

        for edge, prob in zip(edges, succProb):
            adj[edge[0]].append((edge[1], prob))
            adj[edge[1]].append((edge[0], prob))

        # Maxheap cuz Higher priority path required, instead of LOWER cost
        pq = [(1.0, start_node)]      # (probab, node) -> MAXHEAP instead of MINHEAP here
        probab_cache[start_node] = 1.0
        
        while pq:
            pr, node = heapq.heappop_max(pq)
            
            if node == end_node:
                return pr
            
            if pr < probab_cache[node]:
                continue

            for nbr, nbr_pr in adj[node]:
                new_pr = nbr_pr * pr

                if new_pr > probab_cache[nbr]:
                    probab_cache[nbr] = new_pr
                    heapq.heappush_max(pq, (new_pr, nbr))
        
        return probab_cache[end_node]

