"""
Problem Name: Reverse Nodes in k-Group
Difficulty: Hard
Tags: Linked List, Recursion
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18.4 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKthNode(self, curr: Optional[ListNode], k) -> ListNode:
        #print(head.val)
        #return
        #ret = None
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return

        kth = None
        
        dummy = ListNode(0, head)
        groupPrev = dummy # 1 node right before Kth node
        
        while True:
            kth = self.getKthNode(groupPrev, k)
            #print(kth.val)
            
            if not kth:
                break
            groupNext = kth.next

            # Reverse Group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next

