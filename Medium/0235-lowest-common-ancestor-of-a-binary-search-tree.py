"""
Problem Name: Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 56 ms
Memory: 21 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Need to check where the flow goes.
        # Nodes on SAME SIDE or DIFFERENT SIDES
        # WHen flow goes to DIFFERENT SIDES, record current node as LCA

        def LCA(root, p, q) -> 'TreeNode':
            if not root:
                return
            
            # Moving in opposite directions
            if (p.val <= root.val and q.val >= root.val) or (q.val <= root.val and p.val >= root.val):
                print(root.val)
                return root
            elif p.val <= root.val and q.val <= root.val:
                return LCA(root.left, p, q)
            elif p.val >= root.val and q.val >= root.val:
                return LCA(root.right, p, q)
        
        lc = LCA(root, p, q)
        
        return lc

"""
Submission 2
Language: python3
Runtime: 73 ms
Memory: 21.1 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Need to check where the flow goes.
        # Nodes on SAME SIDE or DIFFERENT SIDES
        # WHen flow goes to DIFFERENT SIDES, record current node as LCA

        def LCA(root, p, q) -> 'TreeNode':
            if not root:
                return
            
            # Moving in opposite directions
            if (p.val <= root.val and q.val >= root.val) or (q.val <= root.val and p.val >= root.val):
                print(root.val)
                return root
            # Moving in single direction (left)
            elif p.val <= root.val and q.val <= root.val:
                return LCA(root.left, p, q)
            # Moving in single direction (right)
            elif p.val >= root.val and q.val >= root.val:
                return LCA(root.right, p, q)
        
        lc = LCA(root, p, q)
        
        return lc

"""
Submission 3
Language: python3
Runtime: 68 ms
Memory: 22.8 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q) -> 'TreeNode':
            if not root:
                return 
            
            # Moving in opposite directions
            if (p.val <= root.val and q.val >= root.val) or (q.val <= root.val and p.val >= root.val):
                return root
            # Moving in same direction
            elif p.val <= root.val and q.val <= root.val:
                return dfs(root.left, p, q)
            elif p.val >= root.val and q.val >= root.val:
                return dfs(root.right, p, q)

        lca = dfs(root, p, q)

        return lca

