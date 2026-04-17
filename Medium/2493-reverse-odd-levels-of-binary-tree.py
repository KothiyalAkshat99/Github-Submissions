"""
Problem Name: Reverse Odd Levels of Binary Tree
Difficulty: Medium
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 16 ms
Memory: 22.6 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    def rev(self, root, level):
        if not root:
            return root
        
        if level % 2 != 0:
            if root.left and root.right:
                temp = root.left.val
                root.left.val = root.right.val
                root.right.val = temp
            else:
                return root
        
        self.rev(root.left, 1 + level)
        self.rev(root.right, 1 + level)
    '''

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS APPROACH

        q = deque([root])

        i = 0
        while q:
            if i & 1:
                l, r = 0, len(q) - 1

                while l < r:
                    temp = q[l].val
                    q[l].val = q[r].val
                    q[r].val = temp

                    l += 1 
                    r -= 1

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i += 1
        return root

