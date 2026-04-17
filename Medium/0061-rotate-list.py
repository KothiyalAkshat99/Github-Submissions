"""
Problem Name: Rotate List
Difficulty: Medium
Tags: Linked List, Two Pointers
"""

"""
Submission 1
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
    def rotate(self, head):
        p1 = head
        p2 = p1.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = None
        p2.next = head
        head = p2

        return head

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        
        temp = head
        n = 0 # Length of linked list

        while temp:
            temp = temp.next
            n += 1
        
        k = k % n # number of actual rotations

        if k == 0:
            return head

        while k:
            head = self.rotate(head)
            k -= 1
        
        return head

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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Just need to shift head by (length - k - 1) positions

        if not head:
            return
        
        n = 0
        tail = head
        temp = tail.next
        while temp:
            n += 1
            temp = temp.next
            tail = tail.next
        
        n += 1
        k = k % n # Actual number of rotations

        tail.next = head # Creating a cycle, connecting tail to head of LL

        move_k = n - k - 1

        temp = head
        while move_k:
            temp = temp.next
            move_k -= 1
        
        head = temp.next
        temp.next = None

        return head

