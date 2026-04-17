"""
Problem Name: Two Sum IV - Input is a BST
Difficulty: Easy
Tags: Hash Table, Two Pointers, Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 8 ms
Memory: 19.6 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        stLeft, stRight = [], []
        pushLeft(stLeft, root) # Initially, only holds outer left subtree [5, 3, 2]
        pushRight(stRight, root) # Initially, only holds outer right subtree [5, 6, 7]

        # After the following calls, pops smallest/ largest elements from stacks \
        # and adds their right/ left nodes to stack
        left, right = nextLeft(stLeft), nextRight(stRight) # left = 2, right = 7
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False

