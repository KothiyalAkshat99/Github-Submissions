"""
Problem Name: Reverse Nodes in Even Length Groups
Difficulty: Medium
Tags: Linked List
"""

"""
Submission 1
Language: python3
Runtime: 110 ms
Memory: 40.5 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head
        connector = None
        groupnum = 1
        node_count = 1

        def reverseNodes(node, n):
            prev = node
            curr = node.next
            tail = node.next

            for i in range(n):
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            
            node.next = prev
            tail.next = curr
            return tail

        while curr:
            if groupnum == node_count or not curr.next:
                if node_count % 2 == 0:
                    curr = reverseNodes(connector, node_count)
                connector = curr
                groupnum += 1
                node_count = 0
            
            node_count += 1
            curr = curr.next
        
        return head

