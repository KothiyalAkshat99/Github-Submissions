"""
Problem Name: Serialize and Deserialize BST
Difficulty: Medium
Tags: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Search Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 75 ms
Memory: 21.7 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # DFS using PRE-ORDER or BFS using Queues
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        serialized = ""
        def dfs(node):
            nonlocal serialized
            if not node:
                serialized = serialized + "N,"
                return
            serialized = serialized + f"{node.val},"
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return serialized

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        head = None
        vals = data.split(",")
        self.i = 0 # To keep track of index in vals

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

