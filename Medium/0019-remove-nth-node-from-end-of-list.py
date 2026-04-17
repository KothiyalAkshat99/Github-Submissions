"""
Problem Name: Remove Nth Node From End of List
Difficulty: Medium
Tags: Linked List, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        temp = ListNode(0, head)
        slow, fast = temp, head
        while n > 0 and fast:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next
        #print(slow.val)
        slow.next = slow.next.next

        return temp.next

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0, head)
        p1, p2 = dummy, head
        while n and p2:
            p2 = p2.next
            n -= 1
        
        while p2:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next

        return dummy.next

