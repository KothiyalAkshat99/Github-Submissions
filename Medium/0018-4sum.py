"""
Problem Name: 4Sum
Difficulty: Medium
Tags: Array, Two Pointers, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 315 ms
Memory: 17.8 MB
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # K-Sum Solution

        nums.sort()
        ret, quad = [], []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            
            # base case - 2sum II
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    ret.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        kSum(4, 0, target)
        return ret

