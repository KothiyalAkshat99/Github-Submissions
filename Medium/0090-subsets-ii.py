"""
Problem Name: Subsets II
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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy()) # or subset[::] - Copy of subset
                return
            
            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)

            # All subsets that don't include nums[i]
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]: # Skipping duplicates
                i += 1
            backtrack(i+1, subset)
        
        backtrack(0, [])

        return res

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 18.1 MB
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = [[]]

        def dfs(i, curpath):
            if i == len(nums):
                return
            
            curpath.append(nums[i])
            ret.append(curpath[:])
            dfs(i + 1, curpath)
            
            curpath.pop()
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i + 1, curpath)
        
        dfs(0, [])
        return ret

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = []

        def dfs(i, curpath):
            if i == len(nums):
                ret.append(curpath[:])
                return
            
            curpath.append(nums[i])
            dfs(i + 1, curpath)
            
            curpath.pop()
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i + 1, curpath)
        
        dfs(0, [])
        return ret

"""
Submission 4
Language: python3
Runtime: 0 ms
Memory: 19.5 MB
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # To group duplicates
        ret = []

        def backtrack(curset, i):
            if i == len(nums):
                ret.append(curset[::])
                return
            
            curset.append(nums[i])
            backtrack(curset, i + 1)

            curset.pop()
            # Skipping duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(curset, i + 1)
        
        backtrack([], 0)

        return ret

