"""
Problem Name: Combinations
Difficulty: Medium
Tags: Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 111 ms
Memory: 61.3 MB
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def backtrack(i, curComb):
            if len(curComb) == k:
                ret.append(curComb[::])
                return
            
            for j in range(i, n + 1):
                curComb.append(j)
                backtrack(j + 1, curComb)
                curComb.pop()
        
        backtrack(1, [])

        return ret

