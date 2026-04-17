"""
Problem Name: Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
Tags: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 95 ms
Memory: 89.3 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        # root of tree/ subtree always at index [0] in preorder
        root = TreeNode(preorder[0])
        
        # get index of this root in the inorder traversal
        inorderIndex = inorder.index(preorder[0])

        # elements left of current root in inorder traversal \
        # go into left subtree of current root
        root.left = self.buildTree(preorder[1:inorderIndex + 1], inorder[:inorderIndex])

        # elements right of current root in inorder traversal \
        # go into right subtree of current root
        root.right = self.buildTree(preorder[inorderIndex + 1:], inorder[inorderIndex+1:])

        return root
        
        ''' # Need to do recursive approach

        root = None
        while preorder:
            # root of tree/ subtree always at index [0] in preorder
            r = preorder[0]
            # delete root from preorder
            del preorder[0]

            # Creating new tree node
            newNode = TreeNode(r)

            # Checking if root of newly created tree is empty
            if not root:
                root = newNode

            # get index of this root in the inorder traversal
            inorderIndex = inorder.index(r)

            # checking if the root has elements as left and right subchildren
            if inorderIndex - 1 != -1 and inorderIndex + 1 != len(inorder):
                del inorder[inorderIndex]
        '''
                

"""
Submission 2
Language: python3
Runtime: 87 ms
Memory: 90.9 MB
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # Root of Tree/Subtree is always gonna be at index 0 in PREorder
        # We need to get the index of this root in INorder list
        root = TreeNode(preorder[0]) # Create a new node from root/subroot

        root_InorderIndex = inorder.index(preorder[0])

        # Elements to LEFT of root index go into LEFT subtree of this root
        # Recursively building left subtree now
        # Only passing next root for preorder
        # Only passing LEFT SUBTREE indices for inorder
        root.left = self.buildTree(preorder[1 : root_InorderIndex + 1], inorder[ : root_InorderIndex])

        # Elements to RIGHT of root index go into RIGHT subtree of root
        # Recursively building right subtree
        # Only pass 
        root.right = self.buildTree(preorder[root_InorderIndex + 1 : ], inorder[root_InorderIndex + 1 : ])

        return root

