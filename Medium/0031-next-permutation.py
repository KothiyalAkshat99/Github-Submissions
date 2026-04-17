"""
Problem Name: Next Permutation
Difficulty: Medium
Tags: Array, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Starting from right, find index where arr[i] > arr[i-1]
        # Now find j such that arr[j] = smallest number > arr[i-1]
        # Swap arr[j] <-> arr[i-1]
        # Reverse arr[i:]

        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Starting from right, find index where arr[i] > arr[i-1]
        # Now find j such that arr[j] = smallest number > arr[i-1]
        # Swap arr[j] <-> arr[i-1]
        # Reverse arr[i:]

        # Example - 1, 5, 8, 4, 7, 6, 5, 3, 1
        # arr[i - 1] = 4
        # arr[i] = 7
        # arr[j] = 5
        # After swapping -> 1, 5, 8, 5, 7, 6, 4, 3, 1
        # Reverse after i -> 1, 5, 8, 5, 1, 3, 4, 6, 7

        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 19.4 MB
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Starting from the end, find i such that nums[i + 1] > nums[i]
        # Does not have to be first occurence, keep moving towards front.

        # Now again starting from end, find j such that 
        # nums[j] = lowest number > nums[i]

        # Now swap nums[i] and nums[j]
        # Reverse list starting at i + 1

        if len(nums) <= 2:
            nums.reverse()
            return
        
        i = len(nums) - 2

        # Starting from the end,
        # Find i such that nums[i+1] > nums[i]
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        
        # Starting from the end, find j such that
        # nums[j] is smallest number > nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Swap numbers at positions i and j
            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse the list starting at i + 1
        start = i + 1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

