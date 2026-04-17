"""
Problem Name: Convert Sorted List to Binary Search Tree
Difficulty: Medium
Tags: Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 20.5 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        
        slow_prev = None
        slow = head # Middle of LL
        fast = head # End of LL

        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        
        root = TreeNode(slow.val) # Mid of list = Root of Tree

        slow_prev.next = None

        root.left = self.sortedListToBST(head) # Recursively construct LEFT subtree
        root.right = self.sortedListToBST(slow.next) # Recursively construct RIGHT subtree

        return root

