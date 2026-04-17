"""
Problem Name: Binary Tree Preorder Traversal
Difficulty: Easy
Tags: Stack, Tree, Depth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.5 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # PreOrder - Root, left, right
        
        ret = []

        def preorder(root):
            if not root:
                return
            ret.append(root.val)
            preorder(root.left)
            preorder(root.right)
            return
        
        preorder(root)

        return ret

