"""
Problem Name: Minimize Maximum Pair Sum in Array
Difficulty: Medium
Tags: Array, Two Pointers, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 910 ms
Memory: 31.6 MB
"""
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Since max pair sum has to be MINIMIZED,
        # Use 2 ptr approach to pair small and large elements

        nums.sort()

        left = 0
        right = len(nums) - 1

        ret = 0

        while left < right:
            ret = max(ret, nums[left] + nums[right])
            left += 1
            right -= 1
        
        return ret

