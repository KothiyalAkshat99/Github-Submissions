"""
Problem Name: LRU Cache
Difficulty: Medium
Tags: Hash Table, Linked List, Design, Doubly-Linked List
"""

"""
Submission 1
Language: python3
Runtime: 149 ms
Memory: 78 MB
"""
'''
class Doubly:
    def __init__(self, key, val):
        self.prev = None
        self.key = key
        self.val = val
        self.next = None
'''
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        #self.head = Doubly()
        #self.tail = self.head
        self.count = 0
        self.cache = {}

    def get(self, key: int) -> int:
        # Return value of Key if exists
        print("In GET")
        if key in self.cache:
            '''
            print(f"Key {key} Found")
            #print(self.cache[key])
            print("---")
            '''
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        else: 
            '''
            print(f"Key {key} NOT Found")
            print("---")
            '''
            return -1

    def put(self, key: int, value: int) -> None:
        # Update value of Key if exists
        # Else add Key-Value pair to cache
        # If #Keys > Capacity, DELETE Least Recently Used key.
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        else:
            if self.count == self.capacity:
                first_key = next(iter(self.cache))
                del self.cache[first_key]
                self.cache[key] = value
            else:
                self.cache[key] = value
                self.count += 1
        '''
        print("In PUT")
        print(self.cache)
        print(self.count)
        print("---")
        '''

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Submission 2
Language: python3
Runtime: 143 ms
Memory: 77.9 MB
"""
class Doubly:
    def __init__(self, key:int = 0, value:int = 0):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keymap = {} # Key: Node

        self.head = Doubly() # LRU
        self.tail = Doubly() # MRU
        self.head.right = self.tail
        self.tail.left = self.head

    def insert(self, node):
        prev, next = self.tail.left, self.tail
        prev.right = node
        next.left = node
        node.left = prev
        node.right = next
    
    def remove(self, node):
        prev, next = node.left, node.right
        prev.right = next
        next.left = prev

    def get(self, key: int) -> int:
        if key in self.keymap:
            self.remove(self.keymap[key]) # Removing node
            self.insert(self.keymap[key]) # Inserting to right
            return self.keymap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keymap:
            self.remove(self.keymap[key])
        self.keymap[key] = Doubly(key, value)
        self.insert(self.keymap[key])

        if len(self.keymap) > self.capacity:
            lru = self.head.right
            self.remove(lru)
            del self.keymap[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

