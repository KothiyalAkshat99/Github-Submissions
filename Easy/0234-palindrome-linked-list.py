"""
Problem Name: Palindrome Linked List
Difficulty: Easy
Tags: Linked List, Two Pointers, Stack, Recursion
"""

"""
Submission 1
Language: python3
Runtime: 39 ms
Memory: 34.8 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reverseHead = self.reverseList(slow)

        while reverseHead:
            if head.val != reverseHead.val:
                return False
            head = head.next
            reverseHead = reverseHead.next
        return True

