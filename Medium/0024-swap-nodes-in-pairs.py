"""
Problem Name: Swap Nodes in Pairs
Difficulty: Medium
Tags: Linked List, Recursion
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head 

        dummy = ListNode(0, head) # Dummy
        prev, curr = dummy, head

        while curr and curr.next:
            post = curr.next.next
            sec = curr.next

            sec.next = curr
            curr.next = post
            prev.next = sec

            prev = curr
            curr = post
        
        return dummy.next

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        n1 = head
        n2 = head.next

        temp = n2.next
        n2.next = n1
        n1.next = self.swapPairs(temp)

        return n2

