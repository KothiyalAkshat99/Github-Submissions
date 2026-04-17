"""
Problem Name: Combination Sum II
Difficulty: Medium
Tags: Array, Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 31 ms
Memory: 17.8 MB
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # In regular backtracking, we'll always end up with duplicates.
        # To eliminate duplicates, we SORT the given array
        # In one recursive call, we include all duplicate values of any candidate
        # In other one, we call next DIFFERENT value, skipping all duplicates of current

        ret = []

        # Helps eliminate duplicate combinations
        candidates.sort()
        
        def backTrack(idx, cursum, cnd):
            if cursum == target:
                ret.append(cnd[:])
                return
            if idx == len(candidates) or cursum > target:
                return
            
            # include element at element i
            cnd.append(candidates[idx])
            backTrack(idx + 1, cursum + candidates[idx], cnd)

            # exclude element at element i, as well as duplicates
            cnd.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backTrack(idx + 1, cursum, cnd)
        
        backTrack(0, 0, [])
    
        return ret

"""
Submission 2
Language: python3
Runtime: 35 ms
Memory: 19.7 MB
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        ret = []

        def backtrack(i: int, curList: list, curSum: int):
            if curSum == target:
                ret.append(curList[::])
                return
            
            if i == len(candidates) or curSum > target:
                return
            
            # Including element at index i
            curList.append(candidates[i])
            backtrack(i + 1, curList, curSum + candidates[i])

            curList.pop()
            # Excluding element at index i + ALL of its duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curList, curSum)
        
        backtrack(0, [], 0)

        return ret

