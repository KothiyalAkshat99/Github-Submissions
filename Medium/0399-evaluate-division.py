"""
Problem Name: Evaluate Division
Difficulty: Medium
Tags: Array, String, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Shortest Path
"""

"""
Submission 1
Language: python3
Runtime: 2 ms
Memory: 19.4 MB
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # WEIGHTED GRAPH

        adj = {}    # Maps A -> List of [B,A/B]
        
        for i, equation in enumerate(equations):
            A, B = equation
            
            if A not in adj:
                adj[A] = []
            adj[A].append([B, values[i]])
            
            if B not in adj:
                adj[B] = []
            adj[B].append([A, 1 / values[i]])
    
        
        # For query A/B
        def dfs(src, target, prod):
            if (src not in adj) or (target not in adj) or (src in visited):
                return -1
            
            if src == target:
                return prod
            
            visited.add(src)

            for nb, wt in adj[src]:
                temp = dfs(nb, target, prod * wt)
                if temp != -1:
                    return temp
        
            return -1
        
        ret = []
        for source, target in queries:
            visited = set()
            if source not in adj or target not in adj:
                ret.append(-1)
                continue
            ret.append(dfs(source, target, 1))
    
        return ret

