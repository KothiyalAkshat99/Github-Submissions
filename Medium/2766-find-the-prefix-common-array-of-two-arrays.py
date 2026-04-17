"""
Problem Name: Find the Prefix Common Array of Two Arrays
Difficulty: Medium
Tags: Array, Hash Table, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.9 MB
"""
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hmap = {}
        C = []
        c = 0
        for i in range(0, len(A)):
            
            if A[i] not in hmap:
                hmap[A[i]] = 1
            else:
                c = c+1
                del hmap[A[i]]
            
            if B[i] not in hmap:
                hmap[B[i]] = 1
            else:
                c = c+1
                del hmap[B[i]]
            
            C.append(c)
        
        return C


