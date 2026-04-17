"""
Problem Name: Permutations II
Difficulty: Medium
Tags: Array, Backtracking, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 5 ms
Memory: 20.2 MB
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        counter = Counter(nums) # We're only considering unique elements

        def backtrack(curcomb):
            if len(curcomb) == len(nums):
                ret.append(curcomb[::])
                return
            
            for key in counter:
                if counter[key]:
                    counter[key] -= 1
                    curcomb.append(key)
                    
                    backtrack(curcomb)

                    curcomb.pop()
                    counter[key] += 1
        
        backtrack([])
        return ret

