"""
Problem Name: Partition to K Equal Sum Subsets
Difficulty: Medium
Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.5 MB
"""
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # In this approach,
        # We build buckets 1 at a time
        # O(k * 2^n)
        # 2^n since for each bucket, at each element,
        # we have a choice to include or not.
        # In original approach, this is K^n
        sum_nums = sum(nums)
        if sum_nums % k:
            return False
        
        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i: int, k: int, subsetSum: int) -> bool:
            if k == 0:  # If no subsets left to build
                return True
            if subsetSum == target: # Current subset built
                return backtrack(0, k-1, 0)  # Building new subset now
            
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                if j > i and not used[j-1] and nums[j] == nums[j-1]:
                    continue

                used[j] = True  # Value included
                
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                
                used[j] = False # Backtrack and exclude value

                # If this was start of subset and it failed,
                # immediately break. No need to try other nums.
                if subsetSum == 0:
                    break
            return False

        return backtrack(0, k, 0)

