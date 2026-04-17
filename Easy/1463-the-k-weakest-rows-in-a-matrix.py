"""
Problem Name: The K Weakest Rows in a Matrix
Difficulty: Easy
Tags: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 18.3 MB
"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if not mat:
            return []
        
        rows, cols = len(mat), len(mat[0])
        count = []
        for i in range(rows):
            c = 0
            for j in range(cols):
                if mat[i][j] != 1:
                    break
                c += 1
            count.append([c, i])
        
        count.sort()

        return [j for [i,j] in count[:k]]
        


"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 18.4 MB
"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if not mat:
            return []
        
        rows, cols = len(mat), len(mat[0])

        maxheap = [] # We add [count of soldiers, index] of each row to minheap
        # When size of minheap > k, pop max

        ret = []

        def binSearch(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == 1:
                    l = m + 1
                else:
                    r = m - 1
            return l

        for i in range(rows):
            # Need to count soldiers in each row - Binary Search
            heapq.heappush(ret, [-binSearch(mat[i]), -i])
            if len(ret) > k:
                temp = heapq.heappop(ret)

        sorted_ret = []
        while ret:
            # Pop from the heap to get the strongest element currently in it
            c, i = heapq.heappop(ret)
            # Append the original index
            sorted_ret.append(-i)

        sorted_ret.reverse()
        return sorted_ret

