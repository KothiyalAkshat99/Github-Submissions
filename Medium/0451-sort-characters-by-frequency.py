"""
Problem Name: Sort Characters By Frequency
Difficulty: Medium
Tags: Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting
"""

"""
Submission 1
Language: python3
Runtime: 19 ms
Memory: 19.1 MB
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        maxheap = []
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        for key, value in hashmap.items():
            heapq.heappush(maxheap, (-value, key))
        ret = ""
        while maxheap:
            temp = heapq.heappop(maxheap)
            count = -temp[0]
            while count:
                ret += temp[1]
                count -= 1
        return ret

"""
Submission 2
Language: python3
Runtime: 46 ms
Memory: 39.4 MB
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        # Bucket Sort

        count = Counter(s)
        buckets = defaultdict(list) # freq -> [char]

        for char, cnt in count.items():
            buckets[cnt].append(char)
        
        ret = []
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                ret.append(c * i)
        
        return "".join(ret)

