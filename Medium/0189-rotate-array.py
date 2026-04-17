"""
Problem Name: Rotate Array
Difficulty: Medium
Tags: Array, Math, Two Pointers
"""

"""
Submission 1
Language: python3
Runtime: 7 ms
Memory: 25.6 MB
"""
class Solution:
    def reverse(self, nums: List[int], start, end) -> List[int]:
        i = start
        j = end
        temp = 0
        while i <= j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
        return nums
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums = self.reverse(nums, n-k, n-1)
        nums = self.reverse(nums, 0, n-k-1)
        nums.reverse()
        print(nums)

"""
Submission 2
Language: python3
Runtime: 3 ms
Memory: 25.6 MB
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Reverse first n-k-1 elements of list
        # Reverse last k elements
        # Then reverse entire list

        # Helper Method
        def reverse(left, right):
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        n = len(nums)
        k = k % n

        # Reverse first n-k-1 elements
        reverse(0, n - k - 1)
        
        # Reverse last k elements
        reverse(n-k, n-1)

        # Flip the list
        nums.reverse()
        
        return

