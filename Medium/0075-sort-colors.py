"""
Problem Name: Sort Colors
Difficulty: Medium
Tags: Array, Two Pointers, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0   # Left pointer, used to swap 0's to left
        r = len(nums) - 1 # Right pointer, used to swap 2's to right

        # Swapping 2's to right can potentially end up stranding a 0 in the middle of the array,
        # since we're passing throught left of array in order.
        
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i <= r:
            num = nums[i]
            if num == 0:
                swap(l, i)
                l += 1
            elif num == 2:
                swap(i, r)
                r -= 1
                i -= 1 # In case of a Right swap (2), we would need to check the current i as well
            i += 1 # In case of right swap, +-1 cancels out, i does not change.

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # BUCKET SORT
        hmap = {}

        for i in nums:
            if i not in hmap:
                hmap[i] = 0
            hmap[i] += 1
        
        i = 0
        for val in sorted(hmap.keys()):
            count = hmap[val]
            while count:
                nums[i] = val
                count -= 1
                i += 1
        

