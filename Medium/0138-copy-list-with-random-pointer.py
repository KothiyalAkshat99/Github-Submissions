"""
Problem Name: Copy List with Random Pointer
Difficulty: Medium
Tags: Hash Table, Linked List
"""

"""
Submission 1
Language: python3
Runtime: 44 ms
Memory: 18.6 MB
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {}
        temp = head
        copyhead = None
        #print(type(head))
        while temp:
            newNode = Node(temp.val, None, None)
            hmap[temp] = newNode
            if not copyhead:
                copyhead = newNode
            temp = temp.next
        for i in hmap:
            x = i.next
            r = i.random
            if x:
                copyX = hmap[x]
                hmap[i].next = copyX
            else:
                hmap[i].next = None
            
            if r:
                copyR = hmap[r]
                hmap[i].random = copyR
            else:
                hmap[i].random = None
        
        t = copyhead
        while t:
            print(t.val)
            if t.random:
                print(t.random.val)
            else:
                print("None")
            t = t.next
            print("--")
        
        return copyhead

"""
Submission 2
Language: python3
Runtime: 38 ms
Memory: 18.9 MB
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        hmap = {}

        def makeclones(head):
            if not head:
                return None
            newNode = Node(head.val, None, None)
            newNode.next = makeclones(head.next)
            hmap[head] = newNode

            return newNode
        
        newHead = makeclones(head)

        head1 = head
        head2 = newHead

        while head1:
            if not head1.random:
                print(f"Skipped {head2.val}")
                head1 = head1.next
                head2 = head2.next
                continue
            print(head2.val)
            r = head1.random
            head2.random = hmap[r]
            head1 = head1.next
            head2 = head2.next

        return newHead

        '''
                
        clonehead = None
        temp = head
        hmap = {}

        while temp:
            newNode = Node(temp.val)
            hmap[temp] = newNode
            if not clonehead:
                clonehead = newNode
            temp = temp.next
        '''

