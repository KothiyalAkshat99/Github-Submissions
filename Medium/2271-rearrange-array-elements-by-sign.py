"""
Problem Name: Rearrange Array Elements by Sign
Difficulty: Medium
Tags: Array, Two Pointers, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 47 ms
Memory: 42.4 MB
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        ret = [0] * len(nums)

        posIdx, negIdx = 0, 1

        for i in range(len(nums)):
            if nums[i] >= 0:
                ret[posIdx] = nums[i]
                posIdx += 2
                continue
            ret[negIdx] = nums[i]
            negIdx += 2
        
        return ret

