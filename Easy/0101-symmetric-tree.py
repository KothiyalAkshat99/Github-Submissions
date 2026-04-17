"""
Problem Name: Symmetric Tree
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def check(r1, r2):
            if not r1 and not r2:
                return True
            if (r1 and not r2) or (r2 and not r1):
                return False
            if r1.val != r2.val:
                return False
            
            return check(r1.left, r2.right) and check(r1.right, r2.left)
        
        return check(root.left, root.right)

