"""
Problem Name: Clone Graph
Difficulty: Medium
Tags: Hash Table, Depth-First Search, Breadth-First Search, Graph Theory
"""

"""
Submission 1
Language: python3
Runtime: 33 ms
Memory: 18.3 MB
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        # Using HashMap

        # Hashmap maps Old Node to Clone Node
        # Shows that X (Old Node) has already been cloned, hence placed in the hashmap

        # HashMap -> {OldNode:NewClone}

        if not node:
            return None

        oldToNew = {}

        def dfsClone(node):
            if node in oldToNew:
                return oldToNew[node] # Returns New/Clone Node if clone exists
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for nb in node.neighbors:
                copy.neighbors.append(dfsClone(nb)) # Appending neighbours to clone's neighbours
            
            return copy
        
        return dfsClone(node)

"""
Submission 2
Language: python3
Runtime: 53 ms
Memory: 19.8 MB
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hashmap = {}    # Maps OldNode:NewNode

        def dfsClone(node: Node) -> Node:
            if node in hashmap:
                return hashmap[node]
            
            cloneNode = Node(node.val)
            hashmap[node] = cloneNode

            for nbr in node.neighbors:
                cloneNode.neighbors.append(dfsClone(nbr))
            
            return cloneNode
        
        return dfsClone(node)

