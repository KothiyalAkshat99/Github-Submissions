"""
Problem Name: Reorder List
Difficulty: Medium
Tags: Linked List, Two Pointers, Stack, Recursion
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 23.3 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next: return head
        stk = []
        temp = head
        while temp:
            stk.append(temp)
            temp = temp.next
        n = len(stk)
        temp = head
        for i in range(n//2):
            x = stk.pop()
            nxt = temp.next

            temp.next = x
            x.next = nxt

            temp = nxt
            '''
            x.next = temp.next
            temp.next = x
            if x.next == x:
                break
            temp = x.next
            '''
        temp.next = None


"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 23.3 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # Reverse second half of list, split then merge?
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next # head of second half of list
        prev = slow.next = None # splitting lists

        # Reversing second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merging 2 halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

"""
Submission 3
Language: python3
Runtime: 3 ms
Memory: 27.9 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next # 4. Head of second half of list
        prev = slow.next = None # 3.next = Null now. Lists have been split

        # Reverse second half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Merge halves
        reversed_head = prev
        node = head
        while reversed_head:
            temp1, temp2 = node.next, reversed_head.next
            node.next = reversed_head
            reversed_head.next = temp1
            node = temp1
            reversed_head = temp2

