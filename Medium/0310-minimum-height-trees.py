"""
Problem Name: Minimum Height Trees
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
"""

"""
Submission 1
Language: python3
Runtime: 83 ms
Memory: 38 MB
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # GLOBAL CENTRALIZATION -> Pick middle/close to middle element as root
        # Start from random node A
        # Perform DFS and reach an "end" node B
        # Perform another DFS starting from B to reach an end node C.
        # Now, B and C are at diameters of this tree
        # Our root has to be the middle node in between B and C
        adj = {i:[] for i in range(n)}
        maxheap = []
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False] * n

        def dfs(i: int):
            if visited[i]: return []

            longest_path = []
            visited[i] = True

            for nb in adj[i]:
                if not visited[nb]:
                    path = dfs(nb)
                    if len(path) > len(longest_path):
                        longest_path = path
            longest_path += [i]
            visited[i] = False
            return longest_path
        
        path = dfs(dfs(0)[0])

        return list(set([path[len(path)//2], path[(len(path)-1)//2]]))

