"""
Problem Name: Find Median from Data Stream
Difficulty: Hard
Tags: Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream
"""

"""
Submission 1
Language: python3
Runtime: 121 ms
Memory: 39.7 MB
"""
class MedianFinder:
    # 2 Heap System - Small heap, Large Heap
    # Small Heap contains values <= Median
    # Large Heap contains values >= Median

    # Small Heap is a MAX HEAP
    # Large Heap is a MIN HEAP

    # Heaps should be equal in size (almost equal distribution)

    # All Heap operation aside from peek are O(log n)
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # By default, all values initially pushed to SMALL HEAP (MAXHEAP)
        heapq.heappush(self.small, -num)

        # Making sure every num in Small Heap <= every num inn Large Heap

        if (self.small and self.large and \
            (-1 * self.small[0]) > self.large[0]):
            temp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, temp)
        
        # Checking uneven size
        if len(self.small) > len(self.large) + 1:
            temp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, temp)
        if len(self.large) > len(self.small) + 1:
            temp = heapq.heappop(self.large)
            heapq.heappush(self.small, -temp)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # In case of equal sizes -> even number of digits
        return ((-1 * self.small[0]) + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
Submission 2
Language: python3
Runtime: 139 ms
Memory: 39.7 MB
"""
class MedianFinder:

    def __init__(self):
        self.small = [] # Maxheap - elements smaller than median
        self.large = [] # Minheap - elements larger than median

    def addNum(self, num: int) -> None:
        # Adding to smaller (maxheap) by default
        heapq.heappush(self.small, -num)

        # Need to check if elements are in appropriate heap:
        if self.small and self.large and (-self.small[0]) > self.large[0]:
                temp = heapq.heappop(self.small)
                heapq.heappush(self.large, -temp)

        # Uneven length
        if len(self.small) > len(self.large) + 1:
            temp = heapq.heappop(self.small)
            heapq.heappush(self.large, -temp)

        if len(self.large) > len(self.small) + 1:
            temp = heapq.heappop(self.large)
            heapq.heappush(self.small, -temp)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        elif len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
Submission 3
Language: python3
Runtime: 166 ms
Memory: 41.8 MB
"""
class MedianFinder:

    def __init__(self):
        self.left = []      # maxheap -> elements smaller than median
        self.right = []     # minheap -> elements larger than median

    def addNum(self, num: int) -> None:
        # Pushing to left by default
        heapq.heappush_max(self.left, num)

        # Need to check for 2 cases - 
        # Size(left) - Size(right) > 1 or Size(right) - Size(left) > 1
        # Max of left is not in correct heap

        # Extract max from left and move to right (min-heap)
        # This ensures the new number finds its correct half
        val = heapq.heappop_max(self.left)
        heapq.heappush(self.right, val)
        
        # If right half is larger, move one back to left
        # This keeps left_size >= right_size
        if len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush_max(self.left, val)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return float(self.left[0])
        else:
            # If equal sizes, average the roots
            return (self.left[0] + self.right[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

