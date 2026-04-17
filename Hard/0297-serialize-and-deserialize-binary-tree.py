"""
Problem Name: Serialize and Deserialize Binary Tree
Difficulty: Hard
Tags: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 94 ms
Memory: 22.8 MB
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = []

        def dfs(root):
            if not root:
                ret.append("N")
                return
            ret.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ls = data.split(",")
        self.i = 0

        def dfs():
            if ls[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(ls[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

