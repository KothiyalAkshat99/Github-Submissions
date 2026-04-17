"""
Problem Name: Top K Frequent Elements
Difficulty: Medium
Tags: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
"""

"""
Submission 1
Language: python3
Runtime: 93 ms
Memory: 21.2 MB
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums
        
        mydict = {}
        
        for i in nums:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] += 1

        ret = heapq.nlargest(k, mydict.keys(), key = mydict.get)

        return ret

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 21.3 MB
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # MaxHeap of (freq, element)
        hmap = Counter(nums)
        maxheap = []
        
        for key, value in hmap.items():
            heapq.heappush(maxheap, (-value, key))
        
        ret = []
        while k:
            ret.append(heapq.heappop(maxheap)[1])
            k -= 1
        
        return ret

