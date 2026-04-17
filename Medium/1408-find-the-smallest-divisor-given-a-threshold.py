"""
Problem Name: Find the Smallest Divisor Given a Threshold
Difficulty: Medium
Tags: Array, Binary Search
"""

"""
Submission 1
Language: python3
Runtime: 127 ms
Memory: 22.8 MB
"""
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        ret = 0

        def findResult(divisor):
            result = 0

            for num in nums:
                result += math.ceil(num / divisor)
            
            return result

        while left <= right:
            mid = (left + right) // 2

            result = findResult(mid)
            print(mid)
            print(result)
            print("--")

            if result <= threshold:
                ret = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ret

