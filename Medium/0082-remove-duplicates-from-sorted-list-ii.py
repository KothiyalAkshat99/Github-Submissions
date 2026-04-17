"""
Problem Name: Remove Duplicates from Sorted List II
Difficulty: Medium
Tags: Linked List, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        temp = ListNode(0, head)
        
        l = temp

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                l.next = head.next
            else:
                l = l.next
            head = head.next
        
        return temp.next

