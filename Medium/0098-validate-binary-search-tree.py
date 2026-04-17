"""
Problem Name: Validate Binary Search Tree
Difficulty: Medium
Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.7 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def bst(self, root, left, right):
        if not root:
            return True
        
        if not (root.val < right and root.val > left):
            return False
        
        return self.bst(root.left, left, root.val) and \
        self.bst(root.right, root.val, right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.bst(root, float("-inf"), float("inf"))
        
        '''
        ret = True

        while True:
            x = root.val
            if root.left:
                if root.left.val > root.val:
                    ret = False
                    break
            if root.right:
                if root.right.val < root.val:
                    ret = False
                    break
        '''

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 21 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Providing a range for each recursive call (low to high)
        
        def isValid(root : TreeNode, low : float, high : float) -> bool:
            if not root:
                return True
            
            # Current Node's value must strictly be in between this range
            if not (low < root.val < high):
                return False
            
            return isValid(root.left, low, root.val) and isValid(root.right, root.val, high)
        
        return isValid(root, float('-inf'), float('inf'))

