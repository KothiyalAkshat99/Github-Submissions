"""
Problem Name: Binary Tree Right Side View
Difficulty: Medium
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.6 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        ret = []

        dq = deque()
        dq.append(root)

        while dq:
            l = len(dq)

            for i in range(l):
                r = dq.popleft()
                
                if r.left:
                    dq.append(r.left)
                if r.right:
                    dq.append(r.right)
                if i == l-1:
                    ret.append(r.val)
                            
        return ret
                
                

