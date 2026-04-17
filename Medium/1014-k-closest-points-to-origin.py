"""
Problem Name: K Closest Points to Origin
Difficulty: Medium
Tags: Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect
"""

"""
Submission 1
Language: python3
Runtime: 71 ms
Memory: 22.3 MB
"""
class Solution:
    def pointDistance(self, x1, x2) -> float:
        return sqrt(x1 ** 2 + x2 ** 2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return
        if len(points) == 1:
            return points
        
        hq = []
        hmap = {}
        l = 0
        
        for point in points:
            d = self.pointDistance(point[0], point[1])
            if l < k:
                l += 1
                heapq.heappush(hq, -d)
                if d not in hmap:
                    hmap[d] = [point]
                else:
                    hmap[d].append(point)
            elif l == k:
                temp = -hq[0]
                if d < abs(temp):
                    temp = heapq.heappop(hq)
                    
                    if len(hmap[-temp]) > 1:
                        hmap[-temp].pop(0)
                    else:
                        del hmap[-temp]

                    heapq.heappush(hq, -d)

                    if d not in hmap:
                        hmap[d] = [point]
                    else:
                        hmap[d].append(point)
        
        ret = []
        for key in hmap:
            for value in hmap[key]:
                ret.append(value)
        
        return ret

"""
Submission 2
Language: python3
Runtime: 82 ms
Memory: 25.4 MB
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(sqrt(i**2 + j**2), [i, j]) for [i, j] in points]
        
        heapq.heapify(dist)

        ret = []

        while k:
            point = heapq.heappop(dist)[1]
            ret.append(point)
            k -= 1
        
        return ret

