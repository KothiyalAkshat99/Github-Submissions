"""
Problem Name: Subtree of Another Tree
Difficulty: Easy
Tags: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function
"""

"""
Submission 1
Language: python3
Runtime: 48 ms
Memory: 18.2 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Method to check if trees are same
    def isSameTree(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        
        return (root1.val == root2.val and 
                self.isSameTree(root1.left, root2.left) and
                self.isSameTree(root1.right, root2.right))

    # Base Method to traverse thru tree
    def isST(self, root, subroot) -> bool:
        if not subroot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subroot):
            return True
        return self.isST(root.left, subroot) or self.isST(root.right, subroot)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isST(root, subRoot)

"""
Submission 2
Language: python3
Runtime: 55 ms
Memory: 19.5 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSubtree(self, root, subRoot) -> bool:
        if (root and not subRoot) or (not root and subRoot):
            return False
        
        if not root and not subRoot:
            return True
        
        if root.val != subRoot.val:
            return False
        
        return self.checkSubtree(root.left, subRoot.left) and self.checkSubtree(root.right, subRoot.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.checkSubtree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

"""
Submission 3
Language: python3
Runtime: 47 ms
Memory: 19.7 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSubtree(self, root, subRoot) -> bool:
        if (root and not subRoot) or (not root and subRoot):
            return False
        
        if not root and not subRoot:
            return True
        
        if root.val != subRoot.val:
            return False
        
        return self.checkSubtree(root.left, subRoot.left) and self.checkSubtree(root.right, subRoot.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if root.val == subRoot.val and self.checkSubtree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

