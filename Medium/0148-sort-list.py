"""
Problem Name: Sort List
Difficulty: Medium
Tags: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
"""

"""
Submission 1
Language: python3
Runtime: 191 ms
Memory: 32.9 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Split list into 2 halves
        left = head
        right = self.getMid(head)
        tmp = right.next # Getting middle element and setting next to NULL
        right.next = None
        right = tmp # Right now points to other half of original LL

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow # Middle value
    
    def merge(self, list1, list2):
        tail = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
    
        return dummy.next

