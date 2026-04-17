"""
Problem Name: Swapping Nodes in a Linked List
Difficulty: Medium
Tags: Linked List, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 48 ms
Memory: 40 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        # kth node from start, kth node from end
        kf, kl = None, None

        # one node before kth node from start, one node before kth node from end
        kfprev, klprev = ListNode(0, head), None

        # getting kth node from start 
        while k > 0:
            kfprev = kf
            kf = temp
            temp = temp.next
            k -= 1
        #print(kf.val)
        
        # getting kth node from end
        temp = kf
        kl = head
        while temp.next:
            klprev = kl
            kl = kl.next
            temp = temp.next
        #print(kl.val)
        
        # swapping values
        kf.val, kl.val = kl.val, kf.val
        
        return head

"""
Submission 2
Language: python3
Runtime: 28 ms
Memory: 40.3 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        kthBeg = head
        kthEnd = head

        kthBegPrev = None
        kthEndPrev = None

        while k > 1:
            kthBegPrev = kthBeg
            kthBeg = kthBeg.next
            k -= 1

        temp = kthBeg

        while temp.next:
            kthEndPrev = kthEnd
            kthEnd = kthEnd.next
            temp = temp.next

        kthBeg.val, kthEnd.val = kthEnd.val, kthBeg.val

        return head

