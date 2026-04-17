"""
Problem Name: Delete Leaves With a Given Value
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 20 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.val == target:
            if not root.left and not root.right:
                return None
        
        return root

"""
Submission 2
Language: python3
Runtime: 7 ms
Memory: 20 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Doing POSTORDER checks
        # Go down to leaves by traversing through DFS
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # At current node, for example leaf (where base case returns None)
        if root.val == target:
            # Only return None if leaf -> No left or right subchild
            # In case target is matched but it is non-leaf, return as is.
            if not root.left and not root.right:
                return None
        
        return root

