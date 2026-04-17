"""
Problem Name: Merge k Sorted Lists
Difficulty: Hard
Tags: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 20.2 MB
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSort(self, list1, list2):
        node = ListNode()
        head = node

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        if list1:
            node.next = list1
        else:
            node.next = list2
        
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeSort(l1, l2))
            lists = mergedLists
        
        return lists[0]

