"""
Problem Name: Redundant Connection
Difficulty: Medium
Tags: Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 18.1 MB
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # UNION FIND (With PATH COMPRESSION) to FIND CYCLE
        # Union BY RANK
        # Take Disjointed sets of nodes
        # Traverse edges
        # Start UNION-ing sets

        #O(Vertices + Edges)
        n = len(edges)
        
        # i's parent is i initially
        parent = [i for i in range(n+1)] # ith node -> parent(1-n)
        rank = [1] * (n + 1)

        # Finds parent of n
        def find(n):
            if n == parent[n]:
                return parent[n]
            
            parent[n] = find(parent[n]) # Makes parent of each node the root node
            return parent[n]
        
        def union(n1, n2): # Union by RANK. Merge smaller into larger
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19.7 MB
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(n+1)]
        rank = [1] * (n + 1)

        def find(n: int) -> int:
            if n == parent[n]:
                return parent[n]
            
            parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1: int, n2: int) -> bool:
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

