"""
Problem Name: Reverse Linked List II
Difficulty: Medium
Tags: Linked List
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.6 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        
        # Move l and r to correct positions
        dummy = ListNode(0, head)
        prev_l = dummy
        
        for _ in range(left - 1):
            prev_l = prev_l.next
        
        curr = prev_l.next # left pointer

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev_l.next
            prev_l.next = temp

        return dummy.next

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19.7 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        
        # Move l and r to correct positions
        dummy = ListNode(0, head)
        prev_l = dummy
        
        for _ in range(left - 1):
            prev_l = prev_l.next
        
        l = prev_l.next # left pointer

        r = l
        for _ in range(right - left):
            r = r.next

        next_r = r.next

        prev = None
        curr = l

        # Reverse l to r
        while curr != next_r:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Connect node before sublist to new head
        prev_l.next = prev

        # Connect new tail tp rest of the list after r
        l.next = next_r

        return dummy.next

