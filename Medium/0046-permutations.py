"""
Problem Name: Permutations
Difficulty: Medium
Tags: Array, Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums[:]]
        
        ret = []

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            ret.extend(perms)
            nums.append(n)
        
        return ret

"""
Submission 2
Language: python3
Runtime: 4 ms
Memory: 17.8 MB
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []

        # base case
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            
            ret.extend(perms)
            nums.append(n)
        
        return ret

"""
Submission 3
Language: python3
Runtime: 3 ms
Memory: 17.8 MB
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []

        def backTrack(curpath, curset):
            if len(curpath) == len(nums):
                ret.append(curpath[:])
                return
            
            for num in nums:
                if num in curset:
                    continue
                # Adding number to current path and set
                curpath.append(num)
                curset.add(num)

                backTrack(curpath, curset)

                curset.remove(num)
                curpath.pop()

        
        backTrack([], set())

        return ret

"""
Submission 4
Language: python3
Runtime: 0 ms
Memory: 19.8 MB
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(curpath, curset):
            if len(curpath) == len(nums):
                ret.append(curpath[::])
                return
            
            for num in nums:
                if num in curset:
                    continue
                
                curset.add(num)
                curpath.append(num)

                backtrack(curpath, curset)

                curset.remove(num)
                curpath.pop()
        
        backtrack([], set())
        
        return ret

"""
Submission 5
Language: python3
Runtime: 4 ms
Memory: 19.8 MB
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(curpath, curset):
            if len(curpath) == len(nums):
                ret.append(curpath[::])
                return
            
            for num in nums:
                if num in curset:
                    continue
                
                curset.add(num)
                curpath.append(num)

                backtrack(curpath, curset)

                curset.remove(num)
                curpath.pop()
        
        backtrack([], set())
        
        return ret

