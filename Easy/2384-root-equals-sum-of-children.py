"""
Problem Name: Root Equals Sum of Children
Difficulty: Easy
Tags: Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 30 ms
Memory: 17.4 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.left.val+root.right.val == root.val:
            return True
        else:
            return False

"""
Submission 2
Language: python3
Runtime: 30 ms
Memory: 17.3 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        '''if root.left.val+root.right.val == root.val:
            return True
        else:
            return False'''
        return (root.left.val+root.right.val == root.val)

"""
Submission 3
Language: python3
Runtime: 35 ms
Memory: 17.3 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val==root.left.val+root.right.val

"""
Submission 4
Language: python3
Runtime: 36 ms
Memory: 17.3 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.left.val+root.right.val==root.val

"""
Submission 5
Language: python3
Runtime: 39 ms
Memory: 17.1 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.left.val+root.right.val==root.val

"""
Submission 6
Language: python3
Runtime: 36 ms
Memory: 17.4 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.left.val+root.right.val==root.val

