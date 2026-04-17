"""
Problem Name: Sort an Array
Difficulty: Medium
Tags: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort
"""

"""
Submission 1
Language: python3
Runtime: 591 ms
Memory: 33.3 MB
"""
from random import randint

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quickSort(left, right):
            # Base Case
            if left >= right:
                return
            
            # Random Pivot selected
            pivot = nums[randint(left, right)]

            # Lesser = end of segment with elements < pivot
            # greater = start of segment with elements > pivot
            # current = pointer to scan through
            lesser, greater, current = left - 1, right + 1, left

            while current < greater:
                if nums[current] < pivot:
                    lesser += 1
                    nums[lesser], nums[current] = nums[current], nums[lesser]
                    current += 1
                elif nums[current] > pivot:
                    greater -= 1
                    nums[greater], nums[current] = nums[current], nums[greater]
                else:
                    current += 1
            
            quickSort(left, lesser)
            quickSort(greater, right)
        
        quickSort(0, len(nums) - 1)

        return nums

"""
Submission 2
Language: python3
Runtime: 763 ms
Memory: 24.3 MB
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge Sort - O(n log n)

        def merge(arr, left, mid, right):
            l_arr = arr[left : mid + 1]
            r_arr = arr[mid + 1 : right + 1]

            i, j, k = left, 0, 0

            while j < len(l_arr) and k < len(r_arr):
                if l_arr[j] <= r_arr[k]:
                    arr[i] = l_arr[j]
                    j += 1
                else:
                    arr[i] = r_arr[k]
                    k += 1
                i += 1
            
            while j < len(l_arr):
                arr[i] = l_arr[j]
                j += 1
                i += 1
            
            while k < len(r_arr):
                arr[i] = r_arr[k]
                k += 1
                i += 1
        
        def mergeSort(arr, left, right):
            # Base Case
            if left == right:
                return arr
            
            mid = (left + right) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)

            merge(arr, left, mid, right)

            return arr
        
        return mergeSort(nums, 0, len(nums) - 1)

