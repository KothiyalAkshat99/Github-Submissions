"""
Problem Name: Search in Rotated Sorted Array
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
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        ret = -1

        while(l <= r):
            mid = (l + r) // 2
            if target == nums[mid]:
                    return mid
            if nums[r] < nums[l]:  # Array is rotated
                if nums[mid] >= nums[l]:  # Mid is in the left sorted portion
                    if target < nums[l] or target > nums[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:  # Mid is in the right sorted portion
                    if target >= nums[mid] and target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
            else:  # Normal binary search
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return ret

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 18.2 MB
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            
            # left half is sorted
            if nums[l] <= nums[m]:
                # When element is not in left sorted half
                if target > nums[m] or target < nums[l]: 
                    l = m + 1
                else:
                    r = m - 1
            
            # right half is sorted
            else:
                # When element is not in right sorted half
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 19.6 MB
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # Left Half is completely sorted:
            if nums[l] <= nums[mid]:
                # When element not in left sorted half:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Right half is completely sorted:
            else:
                # Target not in right sorted half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

