"""
Problem Name: Remove Duplicates from Sorted Array
Difficulty: Easy
Tags: Array, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 74 ms
Memory: 18 MB
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Need to do it in-place, without using extra space
        # insertion at i, checking value at j
        i = 1
        for j in range(1, len(nums)):
            # Basically not doing anything in case the 2 values are same
            # As soon as different value is found at j, it is inserted at i
            if nums[j-1]!=nums[j]:
                nums[i] = nums[j]
                i+=1

        return i # Since total distinct values are i+1 as i stops at last insertion

"""
Submission 2
Language: python3
Runtime: 80 ms
Memory: 18 MB
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Need to do it in-place, without using extra space
        i = 1
        for j in range(1, len(nums)):
            if nums[j-1]!=nums[j]:
                nums[i] = nums[j]
                i+=1

        return i

"""
Submission 3
Language: python3
Runtime: 69 ms
Memory: 18 MB
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Need to do it in-place, without using extra space
        i = 1
        for j in range(1, len(nums)):
            if nums[j-1]!=nums[j]:
                nums[i] = nums[j]
                i+=1

        return i

