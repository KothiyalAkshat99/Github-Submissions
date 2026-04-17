"""
Problem Name: Find K-th Smallest Pair Distance
Difficulty: Hard
Tags: Array, Two Pointers, Binary Search, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 23 ms
Memory: 18.5 MB
"""
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Since we only want the distance and not the actual values,
        # We can run a Binary Search in 0-MaxVal search-space.
        nums.sort()
        n = len(nums)

        # Bin-Search range
        low = 0
        high = nums[n-1] - nums[0]

        while low < high:
            mid = (low + high) // 2

            # Couting pairs with distance <= mid
            count = self.count_pairs(nums, mid)

            if count < k:
                low = mid + 1
            else:
                high = mid
        
        return low
    
    # To count #pairs with distance <= maxdist -> Sliding Window
    def count_pairs(self, nums, maxdist) -> int:
        count = 0
        n = len(nums)
        left = 0

        for right in range(n):
            while nums[right] - nums[left] > maxdist:
                left += 1
            count += right - left
        
        return count

