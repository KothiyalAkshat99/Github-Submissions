"""
Problem Name: Kth Smallest Element in a BST
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 21.1 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lst = []
    
    def inorder(self, root) -> list[int]:
        if not root: return
        
        self.inorder(root.left)
        #print(root.val)
        self.lst.append(root.val)
        self.inorder(root.right)
        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root)
        #print(Solution.lst)
        return self.lst[k-1]

