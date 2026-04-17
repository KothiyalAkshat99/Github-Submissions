"""
Problem Name: Reverse Linked List
Difficulty: Easy
Tags: Linked List, Recursion
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18.7 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = None
        b = head
        while b:
            temp = b.next
            b.next = a
            a = b
            b = temp

        return a

