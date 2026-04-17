"""
Problem Name: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Tags: Array, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18 MB
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[0]

        while (l<=r):
            mid = (l + r) // 2
            if nums[r] < nums[l]:
                minimum = min(minimum, nums[mid])
                if nums[mid] >= nums[l]:
                    l = mid + 1
                elif nums[mid] < nums[l]:
                    r = mid
            else:
                minimum = min(minimum, nums[l])
                break

        return minimum

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19.5 MB
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ret = nums[l]

        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:
            mid = (l + r) // 2

            # Pivot point or point of rotation
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                ret = nums[mid + 1]
                break
            # When mid is min
            if mid > 0 and nums[mid] < nums[mid - 1]:
                ret = nums[mid]
                break
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        return ret

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 19.6 MB
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # Just keep on shrinking the window
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        return nums[l]


