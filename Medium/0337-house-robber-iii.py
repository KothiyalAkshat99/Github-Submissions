"""
Problem Name: House Robber III
Difficulty: Medium
Tags: Dynamic Programming, Tree, Depth-First Search, Binary Tree
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
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # return pair: [withRoot, withoutRoot]
        def dfs(root):
            if not root:
                return [0, 0]
            
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            # Taking index 1 of both left and right pair
            # Because if we take CURRENT ROOT,\
            # we cannot take root of children
            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]
        
        return max(dfs(root))

