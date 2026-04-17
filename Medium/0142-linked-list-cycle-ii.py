"""
Problem Name: Linked List Cycle II
Difficulty: Medium
Tags: Hash Table, Linked List, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 53 ms
Memory: 19.6 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # when a cycle exists
                # Reset any (slow/fast) pointer to head
                # In this case, distance here between \
                # SLOW to CYCLE START = HEAD to CYCLE START
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

"""
Submission 2
Language: python3
Runtime: 49 ms
Memory: 19.4 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # when a cycle exists
                # Reset any (slow/fast) pointer to head
                # In this case, distance here between \
                # SLOW to CYCLE START = HEAD to CYCLE START
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

"""
Submission 3
Language: python3
Runtime: 39 ms
Memory: 20 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        hmap = {}
        idx = 0
        while head.next:
            if head not in hmap:
                hmap[head] = idx
                idx += 1
                head = head.next
                continue
            return head
        
        return None

"""
Submission 4
Language: python3
Runtime: 47 ms
Memory: 19.6 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        # Distance between \
        # HEAD and START of Cycle = SLOW/FAST converge to START of Cycle
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # When a cycle exists
            if slow == fast:
                fast = head # Reset slow/fast to head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow # or return slow. Same thing
                # They converge at Start of Cycle
        
        return None

