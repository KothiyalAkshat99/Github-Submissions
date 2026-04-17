"""
Problem Name: Subsets
Difficulty: Medium
Tags: Array, Backtracking, Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        # i = index of number in list
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Decision not to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0) # First Value

        return res

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19.5 MB
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(i: int, subset: list):
            if i == len(nums):
                ret.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)

            subset.pop()
            backtrack(i + 1, subset)            

            
        
        backtrack(0, [])

        return ret

