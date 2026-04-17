"""
Problem Name: Merge Triplets to Form Target Triplet
Difficulty: Medium
Tags: Array, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 62 ms
Memory: 55.3 MB
"""
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ls = []
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or \
                triplets[i][1] > target[1] or \
                triplets[i][2] > target[2]:
                continue
            ls.append(triplets[i])
        if not ls:
            return False
        print(ls)
        n1, n2, n3 = 0,0,0
        for i in ls:
            if i[0] == target[0]:
                n1 = 1
            if i[1] == target[1]:
                n2 = 1
            if i[2] == target[2]:
                n3 = 1
        if not n1 or not n2 or not n3:
            return False
        return True

