"""
Problem Name: Diameter of Binary Tree
Difficulty: Easy
Tags: Tree, Depth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 20.8 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    def subtreeLength(self, root) -> int:
        if not root: return 0

        l1 = 1 + subtreeLength(self, root.left, 0)
        l2 = 1 + subtreeLength(self, root.right, 0)
        maxL = max(maxl, l1 + l2)

        return maxL
    '''

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Potential Approach - 
        # Calculate max height of left and right subtree at EACH SUBTREE (RECURSIVE)

        # Need to keep a global max as originally planned

        self.maxL = 0

        # Returns height at each level
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            # This is the diameter
            self.maxL = max(self.maxL, left + right)

            # Return height, not diameter
            return 1 + max(left, right)
        
        dfs(root)
        
        return self.maxL

"""
Submission 2
Language: python3
Runtime: 4 ms
Memory: 20.8 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxlen = 0

        def diameterCalc(root) -> int:
            if not root:
                return 0
            
            left = diameterCalc(root.left)
            right = diameterCalc(root.right)

            self.maxlen = max(self.maxlen, left + right)

            return 1 + max(left, right)
        
        diameterCalc(root)

        return self.maxlen

"""
Submission 3
Language: python3
Runtime: 4 ms
Memory: 22.1 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxlen = 0

        def diameter(root) -> int:
            if not root:
                return 0
            
            leftlen = diameter(root.left)
            rightlen = diameter(root.right)

            nonlocal maxlen
            maxlen = max(maxlen, leftlen + rightlen)

            return 1 + max(leftlen, rightlen)
        
        diameter(root)
        return maxlen

