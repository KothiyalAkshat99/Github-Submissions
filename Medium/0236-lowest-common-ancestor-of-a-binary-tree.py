"""
Problem Name: Lowest Common Ancestor of a Binary Tree
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 51 ms
Memory: 22.2 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traversal(root, p, q):
            if not root or root == p or root == q:
                return root
            left = traversal(root.left, p, q)
            right = traversal(root.right, p, q)
            if left and right:
                return root
            return left or right
        
        return traversal(root, p, q)

