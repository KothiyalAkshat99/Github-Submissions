"""
Problem Name: Count Good Nodes in Binary Tree
Difficulty: Medium
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 151 ms
Memory: 32.1 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def gN(self, root, m) -> int:
        if not root:
            return 0
        
        ret = 1 if root.val >= m else 0
        m = max(m, root.val)
        
        ret += self.gN(root.left, m)
        ret += self.gN(root.right, m)

        return ret
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.gN(root, root.val)

"""
Submission 2
Language: python3
Runtime: 137 ms
Memory: 32.1 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxval) -> int:
            if not root:
                return 0
            
            ret = 1 if root.val >= maxval else 0
            maxval = max(maxval, root.val)
            
            ret += dfs(root.left, maxval)
            ret += dfs(root.right, maxval)

            return ret

        return dfs(root, root.val)

