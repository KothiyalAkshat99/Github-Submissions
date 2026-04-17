"""
Problem Name: Kth Largest Element in a Stream
Difficulty: Easy
Tags: Tree, Design, Binary Search Tree, Heap (Priority Queue), Binary Tree, Data Stream
"""

"""
Submission 1
Language: python3
Runtime: 19 ms
Memory: 23.5 MB
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest Ints

        self.minHeap, self.k = nums, k

        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
Submission 2
Language: python3
Runtime: 16 ms
Memory: 25.5 MB
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.minheap = nums
        
        heapq.heapify(nums)

        while len(self.minheap) > self.capacity:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)

        if len(self.minheap) > self.capacity:
            heapq.heappop(self.minheap)
        
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
Submission 3
Language: python3
Runtime: 26 ms
Memory: 25.4 MB
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        heapq.heapify(self.minheap)
        self.k = k
        
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)

        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        
        return self.minheap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

