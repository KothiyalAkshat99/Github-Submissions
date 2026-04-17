"""
Problem Name: Maximum Depth of Binary Tree
Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 2 ms
Memory: 19 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def md(self, root, l) -> int:
        if not root: return 0

        ll, lr = 0, 0

        ll = 1 + self.md(root.left, 0)
        lr = 1 + self.md(root.right, 0)

        return max(ll, lr)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l = self.md(root, 0)

        return l

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def md(self, root) -> int:
        if not root: return 0

        ll, lr = 0, 0

        ll = 1 + self.md(root.left)
        lr = 1 + self.md(root.right)

        return max(ll, lr)
        

        #return 1 + max(self.md(node.left))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l = self.md(root)

        return l

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 19 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def md(self, root) -> int:
        if not root: return 0

        ll, lr = 0, 0

        ll = 1 + self.md(root.left)
        lr = 1 + self.md(root.right)

        return max(ll, lr)

        # In a single line - 
        # return 1 + max(self.md(root.left), self.md(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l = self.md(root)

        return l

"""
Submission 4
Language: python3
Runtime: 0 ms
Memory: 19 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # USING BFS (LEVEL-ORDER)
        if not root: return 0

        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        
        return level

"""
Submission 5
Language: python3
Runtime: 3 ms
Memory: 19.3 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # USING BFS (LEVEL-ORDER) - Iterative
        if not root: return 0

        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        
        return level

"""
Submission 6
Language: python3
Runtime: 6 ms
Memory: 19 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Using ITERATIVE DFS - Using STACK - PREORDER(easiest for iterative)
        
        stk = [[root, 1]] # [node, depth]
        res = 0

        while stk:
            node, depth = stk.pop()

            if node:
                res = max(res, depth)
                stk.append([node.left, depth + 1])
                stk.append([node.right, depth + 1])
            
        return res

"""
Submission 7
Language: python3
Runtime: 3 ms
Memory: 20.2 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lenleft = 1 + self.maxDepth(root.left)
        lenright = 1 + self.maxDepth(root.right)
        return max(lenleft, lenright)

"""
Submission 8
Language: python3
Runtime: 3 ms
Memory: 20.4 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        dq = deque([root])

        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1
        
        return level

