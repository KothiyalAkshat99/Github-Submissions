"""
Problem Name: Partition Labels
Difficulty: Medium
Tags: Hash Table, Two Pointers, String, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.9 MB
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # char -> last found index

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        ret = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            if lastIndex[c] > end:
                end = lastIndex[c]
            
            if i == end:
                ret.append(size) # a partition has been completed
                size = 0 # for new partition
        
        return ret

