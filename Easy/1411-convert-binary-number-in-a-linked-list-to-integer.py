"""
Problem Name: Convert Binary Number in a Linked List to Integer
Difficulty: Easy
Tags: Linked List, Math
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
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        temp = head
        n = 0
        while temp:
            n += 1
            temp = temp.next
        
        ret = 0
        temp = head
        while temp:
            ret += temp.val * 2**(n-1)
            n -= 1
            temp = temp.next
        
        return ret

