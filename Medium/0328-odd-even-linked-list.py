"""
Problem Name: Odd Even Linked List
Difficulty: Medium
Tags: Linked List
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.1 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        odd.next = even_head
        return head

