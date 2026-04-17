"""
Problem Name: Binary Tree Level Order Traversal
Difficulty: Medium
Tags: Tree, Breadth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18.4 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        dq = deque()
        dq.append(root)

        res = []
        
        while dq:
            l = len(dq)
            level = []

            for i in range(l):
                r = dq.popleft()
                level.append(r.val)

                if r.left:
                    dq.append(r.left)
                if r.right:
                    dq.append(r.right)
            
            res.append(level)

        return res

"""
Submission 2
Language: python3
Runtime: 3 ms
Memory: 20.1 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret = []

        dq = deque()
        dq.append(root)
        
        while dq:
            n = len(dq) # Current length of deque
            level = []

            # For loop used instead of while
            # This is because even though we're adding subnodes in same loop,
            # the loop only executes for n number of times, which is pre-determined by n

            # For first execution, n = 1, x = root
            # x appended to level
            # left and right if available, appended to deque
            # Now deque has next level after root
            for i in range(n):
                x = dq.popleft()
                level.append(x.val)

                # So, even though we're appending 
                if x.left:
                    dq.append(x.left)
                if x.right:
                    dq.append(x.right)
            
            ret.append(level)
        
        return ret

