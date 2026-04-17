"""
Problem Name: Insert into a Binary Search Tree
Difficulty: Medium
Tags: Tree, Binary Search Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 21.2 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        

        return root

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 21.2 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        curr = root
        
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right

