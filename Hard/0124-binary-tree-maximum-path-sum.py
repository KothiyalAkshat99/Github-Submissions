"""
Problem Name: Binary Tree Maximum Path Sum
Difficulty: Hard
Tags: Dynamic Programming, Tree, Depth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 22.9 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        s = float("-inf")

        def maxsum(root) -> int:
            nonlocal s
            if not root: return 0

            lsum = max(maxsum(root.left), 0) # Ensures 0/ +ve gain to path in case of -ve values
            rsum = max(maxsum(root.right), 0)

            s = max(s, lsum + rsum + root.val) # global max vs current max

            return root.val + max(lsum, rsum)
        
        maxsum(root)
        
        return s

"""
Submission 2
Language: python3
Runtime: 8 ms
Memory: 24 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float("-inf")

        def dfs(root):
            if not root:
                return 0
            
            nonlocal maxsum

            l = max(dfs(root.left), 0)
            r = max(dfs(root.right), 0)

            # Comparing against global max path sum
            maxsum = max(maxsum, l + r + root.val)

            return root.val + max(l, r)
        
        dfs(root)

        return maxsum

