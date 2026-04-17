"""
Problem Name: Number of Subsequences That Satisfy the Given Sum Condition
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 6291 ms
Memory: 28.3 MB
"""
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if not nums or not target:
            return 0
        
        n = len(nums)
        nums.sort()
        count = 0
        mod = (10 ** 9 + 7)

        left = 0
        right = n-1

        while left <= right:
            while (nums[left] + nums[right]) > target and left <= right:
                right -= 1
            if left <= right:
                count += (2 ** (right - left))
                count %= mod
            left += 1
        return count

"""
Submission 2
Language: python3
Runtime: 157 ms
Memory: 27.7 MB
"""
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if not nums or not target:
            return 0
        
        n = len(nums)
        nums.sort()
        count = 0
        mod = (10 ** 9 + 7)

        left = 0
        right = n-1

        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + pow(2, right - left, mod)) % mod
                left += 1
            else:
                right -= 1
       
        return count

        '''
        while left <= right:
            while (nums[left] + nums[right]) > target and left <= right:
                right -= 1
            if left <= right:
                count += (2 ** (right - left))
                count %= mod
            left += 1
        return count
        '''
        

