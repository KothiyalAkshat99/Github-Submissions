"""
Problem Name: Delete Node in a BST
Difficulty: Medium
Tags: Tree, Binary Search Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 22.1 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:   # If node found and no left subchild, return right subchild
                return root.right
            elif not root.right:    # If node found and no right subchild, return left 
                return root.left
            
            # Find min from right subtree/subchild
            # This node with min value in RIGHT subtree replaces the deleted node
            # Then we recursively call delete for this min node
            curr = root.right
            while curr.left:
                curr = curr.left 
            root.val = curr.val
            # Recursively calling delete for min value subnode \
            # to be deleted from right subtree of current root (node to be deleted)
            root.right = self.deleteNode(root.right, root.val)
        
        return root

