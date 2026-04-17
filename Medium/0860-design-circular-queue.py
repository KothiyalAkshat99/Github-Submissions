"""
Problem Name: Design Circular Queue
Difficulty: Medium
Tags: Array, Linked List, Design, Queue
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 20.3 MB
"""
class ListNode:
    def __init__(self, val, prev: ListNode = None, nxt: ListNode = None):
        self.val = val
        self.prev = prev
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = ListNode(-1)
        self.tail = ListNode(-2)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.space = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        cur = ListNode(value, self.tail.prev, self.tail)
        self.tail.prev.next = cur
        self.tail.prev = cur
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        removed_node = self.head.next
        new_front = removed_node.next
        self.head.next = new_front
        new_front.prev = self.head
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def isFull(self) -> bool:
        return self.space == 0

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

