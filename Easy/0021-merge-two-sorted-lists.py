"""
Problem Name: Merge Two Sorted Lists
Difficulty: Easy
Tags: Linked List, Recursion
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.9 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        head = ListNode()
        h = head
        while list1 and list2:
            if list1.val <= list2.val:
                h.val = list1.val
                list1 = list1.next
            elif list2.val < list1.val:
                h.val = list2.val
                list2 = list2.next
            if list1 or list2:
                h.next = ListNode()
                h = h.next
        
        while list1:
            h.val = list1.val
            list1 = list1.next
            if list1:
                h.next = ListNode()
                h = h.next
        
        while list2:
            h.val = list2.val
            list2 = list2.next
            if list2:
                h.next = ListNode()
                h = h.next
        
        return head

"""
Submission 2
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        if not list1:
            return list2
        if not list2:
            return list1 
        head = ListNode()
        h = head
        while list1 and list2:
            if list1.val <= list2.val:
                h.val = list1.val
                list1 = list1.next
            elif list2.val < list1.val:
                h.val = list2.val
                list2 = list2.next
            if list1 or list2:
                h.next = ListNode()
                h = h.next
        
        while list1:
            h.val = list1.val
            list1 = list1.next
            if list1:
                h.next = ListNode()
                h = h.next
        
        while list2:
            h.val = list2.val
            list2 = list2.next
            if list2:
                h.next = ListNode()
                h = h.next
        
        return head

"""
Submission 3
Language: python3
Runtime: 3 ms
Memory: 19.4 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode(0, None)
        temp = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = ListNode(list1.val)
                temp = temp.next
                list1 = list1.next
            elif list2.val < list1.val:
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next
        
        while list1:
            temp.next = ListNode(list1.val)
            temp = temp.next
            list1 = list1.next
        
        while list2:
            temp.next = ListNode(list2.val)
            temp = temp.next
            list2 = list2.next
        
        return dummy.next

