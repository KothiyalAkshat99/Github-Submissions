"""
Problem Name: Combination Sum
Difficulty: Medium
Tags: Array, Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 17.9 MB
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []    
        
        def backTrack(i, cur, s):
            if s == target:
                ret.append(cur.copy())
                return
            if i >= len(candidates) \
                or s > target:
                return

            # Route 1 -> Adding i
            cur.append(candidates[i])
            backTrack(i, cur, s + candidates[i])

            # Route 2 -> Not adding i
            # To weed out permutations
            cur.pop()
            backTrack(i + 1, cur, s)


        backTrack(0, [], 0)
        return ret

"""
Submission 2
Language: python3
Runtime: 15 ms
Memory: 17.8 MB
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []    
        
        def backTrack(i, cur, s):
            if s == target:
                ret.append(cur.copy())
                return
            if i >= len(candidates) \
                or s > target:
                return

            # Route 1 -> Adding i
            cur.append(candidates[i])
            # Recursive call using 'i' and not 'i+1' because UNLIMITED USAGE of current elem
            backTrack(i, cur, s + candidates[i])

            # Route 2 -> Not adding i
            # To weed out permutations
            cur.pop()
            backTrack(i + 1, cur, s)


        backTrack(0, [], 0)
        return ret

"""
Submission 3
Language: python3
Runtime: 12 ms
Memory: 19.7 MB
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        def backtrack(i: int, curComb: list[int], curSum: int):
            if curSum == target:
                ret.append(curComb[::])
                return
            
            if curSum > target or i >= len(candidates):
                return
            
            # We can take current digit unlimited number of times
            curComb.append(candidates[i])
            backtrack(i, curComb, curSum + candidates[i])

            curComb.pop()
            backtrack(i + 1, curComb, curSum)
        
        backtrack(0, [], 0)
        return ret

