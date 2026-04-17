"""
Problem Name: Add Two Numbers
Difficulty: Medium
Tags: Linked List, Math, Recursion
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 18.1 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insert(self, tl:"End", node):
        tl.next = node
        tl = tl.next
        return tl

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        h3 = None
        carry = 0
        hmap = {}
        while h1 and h2:
            s = h1.val + h2.val + carry
            carry = s // 10
            s = s % 10
            newNode = ListNode(s)
            if not h3:
                h3 = newNode
            hmap[newNode] = None
            h1 = h1.next
            h2 = h2.next
        
        while h1:
            s = h1.val + carry
            carry = s // 10
            s = s % 10
            newNode = ListNode(s)
            hmap[newNode] = None
            h1 = h1.next
        
        while h2:
            s = h2.val + carry
            carry = s // 10
            s = s % 10
            newNode = ListNode(s)
            hmap[newNode] = None
            h2 = h2.next
        
        if carry != 0:
            newNode = ListNode(carry)
            hmap[newNode] = None
        
        tl = h3
        for i in hmap:
            if i == h3:
                continue
            tl = self.insert(tl, i)
            
        return h3

"""
Submission 2
Language: python3
Runtime: 8 ms
Memory: 18.1 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        h3 = None
        tl = None
        carry = 0
        
        while h1 or h2 or carry:
            s = carry
            if h1:
                s = s + h1.val
                h1 = h1.next
            if h2:
                s = s + h2.val
                h2 = h2.next
            
            carry = s // 10
            s = s % 10
            newNode = ListNode(s)
            if not h3:
                h3 = newNode
                tl = h3
            else:
                tl.next = newNode
                tl = tl.next
            
        return h3

