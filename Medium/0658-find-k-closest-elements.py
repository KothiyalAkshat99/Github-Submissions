"""
Problem Name: Find K Closest Elements
Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue)
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.2 MB
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        # Binary Search for optimal starting index of k-element window.
        # Window = arr[low : low + k]
        low = 0
        high = n - k
        
        while low < high:
            mid = (high + low) // 2
            if arr[mid] == arr[mid + k]:
                if arr[mid] < x:low = mid + 1
                else:high = mid
            elif abs(x-arr[mid]) <= abs(x - arr[mid + k]):
                high = mid
            else:
                low = mid + 1
        
        return arr[low : low + k]

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 18.9 MB
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # We're trying to find the lower bound range of the required window of size k
        # Using Binary Search, our MID = lower bound range
        
        # For each mid, we're checking if the element at mid(start of window) is closer than \
        # the first element outside of this window

        n = len(arr)
        left, right = 0, n-k
        
        while left < right:
            mid = (left + right) // 2

            # x - arr[mid] = Difference between x and first element of potential window
            # arr[mid + k] = Difference between x and first element OUTSIDE of window
            # This condition means that value to right of window is CLOSER
            # So we shift lower bound to right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left : left + k]

