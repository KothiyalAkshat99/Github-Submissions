"""
Problem Name: Minimum Operations to Make Median of Array Equal to K
Difficulty: Medium
Tags: Array, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 91 ms
Memory: 41.2 MB
"""
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)
        medIdx = n // 2
        med = nums[medIdx]

        if med == k: return 0

        op = 0 # Number of operations
        op += abs(k-med)
        nums[medIdx] = k
        med = k

        for i in range(len(nums)):
            if i == medIdx: continue

            if i < medIdx:
                if nums[i] > med:
                    op += abs(nums[i]-med)
            elif i > medIdx:
                if nums[i] < med:
                    op += abs(nums[i]-med)
        
        return op

