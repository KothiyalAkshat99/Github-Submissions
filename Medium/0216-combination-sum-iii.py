"""
Problem Name: Combination Sum III
Difficulty: Medium
Tags: Array, Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 2 ms
Memory: 17.9 MB
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # k = size of subsequence of [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # n = target sum
        ret = []

        def recur(curnum, cursum, path):
            if len(path) == k:
                if cursum == n:
                    ret.append(path[::])
                return
            
            if cursum > n or curnum > 9:
                return
            
            # Adding current element/number
            path.append(curnum)
            recur(curnum + 1, cursum + curnum, path)

            # Not adding current element/number
            path.pop()
            recur(curnum + 1, cursum, path)
        
        recur(1, 0, [])

        return ret

