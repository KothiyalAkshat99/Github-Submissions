"""
Problem Name: Reverse Pairs
Difficulty: Hard
Tags: Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set
"""

"""
Submission 1
Language: python3
Runtime: 943 ms
Memory: 23.7 MB
"""
class Solution:
    def merge(self, nums, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        
        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        while right <= high:
            temp.append(nums[right])
            right += 1
        
        for i in range(low, high + 1):
            nums[i] = temp[i - low]
    
    def countPairs(self, nums, low, mid, high):
        right = mid + 1
        count = 0
        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            count += right - (mid + 1)
        return count
    
    def mergeSort(self, nums, low, high):
        count = 0
        
        if low == high:
            return count
        
        mid = (low + high) // 2
        
        count += self.mergeSort(nums, low, mid)
        count += self.mergeSort(nums, mid + 1, high)

        count += self.countPairs(nums, low, mid, high)

        self.merge(nums, low, mid, high)

        return count
    
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return

        return self.mergeSort(nums, 0, len(nums)-1)    

