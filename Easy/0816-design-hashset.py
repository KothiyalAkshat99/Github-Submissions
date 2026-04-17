"""
Problem Name: Design HashSet
Difficulty: Easy
Tags: Array, Hash Table, Linked List, Design, Hash Function
"""

"""
Submission 1
Language: python3
Runtime: 79 ms
Memory: 24.2 MB
"""
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)] # Max size/ keys
        # Each element is a linked-list
        # First element of linked-list is a dummy

    def add(self, key: int) -> None:
        curr = self.set[key % len(self.set)]

        # Going to end of Linked-List
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.set[key % len(self.set)]

        # Going to end of Linked-List
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.set[key % len(self.set)]

        # Going to end of Linked-List
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

