"""
Problem Name: Largest Number
Difficulty: Medium
Tags: Array, String, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 17.7 MB
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return f"{nums[0]}"
        
        nums = [str(i) for i in nums]

        def comp(n, m):
            if n + m > m + n:
                return -1
            else:
                return 1

        nums = sorted(nums, key = cmp_to_key(comp))
        return str(int("".join(nums)))

