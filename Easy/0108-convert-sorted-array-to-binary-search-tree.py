"""
Problem Name: Convert Sorted Array to Binary Search Tree
Difficulty: Easy
Tags: Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 19 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def BSTConstruct(l, r):
            if l > r:
                return None
            
            k = (l + r) // 2

            root = TreeNode(nums[k]) # Middle element will be root of tree/subtree
            root.left = BSTConstruct(l, k-1)
            root.right = BSTConstruct(k+1, r)
            return root
        
        return BSTConstruct(0, len(nums)-1)

