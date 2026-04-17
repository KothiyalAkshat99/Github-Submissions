"""
Problem Name: Median of Two Sorted Arrays
Difficulty: Hard
Tags: Array, Binary Search, Divide and Conquer
"""

"""
Submission 1
Language: python3
Runtime: 24 ms
Memory: 18 MB
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        # 2 heap structure
        # Maxheap and Minheap
        # Maxheap -> elements <= median
        # Minheap -> elements >= median

        leftheap = [] # maxheap
        rightheap = [] # minheap

        def insertAndMerge(num):
            # Adding to smaller (maxheap) by default
            heapq.heappush(leftheap, -num)

            # Need to check if elements are in appropriate heap:
            if leftheap and rightheap and (-leftheap[0]) > rightheap[0]:
                    temp = heapq.heappop(leftheap)
                    heapq.heappush(rightheap, -temp)

            # Uneven length check
            if len(leftheap) > len(rightheap) + 1:
                temp = heapq.heappop(leftheap)
                heapq.heappush(rightheap, -temp)

            if len(rightheap) > len(leftheap) + 1:
                temp = heapq.heappop(rightheap)
                heapq.heappush(leftheap, -temp)

        while nums1 or nums2:
            if nums1:
                insertAndMerge(nums1.pop(0))
            if nums2:
                insertAndMerge(nums2.pop(0))
        #print(leftheap)
        #print(rightheap)
        if len(leftheap) > len(rightheap):
            return -leftheap[0]
        elif len(leftheap) < len(rightheap):
            return rightheap[0]
        elif len(leftheap) == len(rightheap):
            return (-leftheap[0] + rightheap[0]) / 2

