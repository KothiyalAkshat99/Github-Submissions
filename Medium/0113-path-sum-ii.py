"""
Problem Name: Path Sum II
Difficulty: Medium
Tags: Backtracking, Tree, Depth-First Search, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.1 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ret = []

        curpath = []

        def dfs(root, cursum):
            if not root:
                return

            curpath.append(root.val)
            cursum += root.val

            if not root.left and not root.right and cursum == targetSum:
                ret.append(curpath[:])
            
            dfs(root.left, cursum)
            dfs(root.right, cursum)

            # Backtracking step
            # Remove current node from path
            curpath.pop()
        
        dfs(root, 0)

        return ret

"""
Submission 2
Language: python3
Runtime: 1 ms
Memory: 19 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        ret = []

        def dfs(root, cursum, curpath):
            if not root:
                return

            curpath.append(root.val)
            cursum += root.val

            if not root.left and not root.right and cursum == targetSum:
                ret.append(curpath[:])
                curpath.pop()
                return
            
            dfs(root.left, cursum, curpath)
            dfs(root.right, cursum, curpath)

            # Backtracking step
            # Remove current node from path
            curpath.pop()
        
        dfs(root, 0, [])

        return ret

