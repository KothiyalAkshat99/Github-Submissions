"""
Problem Name: Balanced Binary Tree
Difficulty: Easy
Tags: Tree, Depth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 7 ms
Memory: 19 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBal(self, root):
        if not root:
                return [True, 0]
        
        left = self.isBal(root.left)
        right = self.isBal(root.right)

        balanced = (left[0] and right[0]) and abs(left[1]-right[1]) <= 1

        return [balanced, 1 + max(left[1], right[1])]
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self.isBal(root)[0]

"""
Submission 2
Language: python3
Runtime: 7 ms
Memory: 20.7 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            # Checking for 2 Conditions in 1 go - 
            # Condition 1 -> Both left and right subtree are balanced (Both True)
            # Condition 2 -> Length disparity in between both subtrees at current level
            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1

            # Returning New modified balanced bool var along with max of current subtree lengths
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

