"""
Problem Name: Squares of a Sorted Array
Difficulty: Easy
Tags: Array, Two Pointers, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 7 ms
Memory: 19.7 MB
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])

"""
Submission 2
Language: python3
Runtime: 31 ms
Memory: 19.9 MB
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        if len(nums) == 1:
            return [nums[0]**2]
        n = len(nums)

        ret = [0] * n
        k = n - 1

        l = 0
        r = n - 1
        
        while l <= r:
            num1 = abs(nums[l] ** 2)
            num2 = abs(nums[r] ** 2)
            #print(num1)
            #print(num2)
            print("")
            if num1 > num2:
                ret[k] = num1
                k -= 1
                l += 1
            elif num1 < num2:
                ret[k] = num2
                k -= 1
                r -= 1
            else:
                ret[k] = num1
                k -= 1
                if l != r:
                    ret[k] = num2
                    k -= 1
                    r -= 1
                l += 1
            #print(ret)
        
        return ret

"""
Submission 3
Language: python3
Runtime: 7 ms
Memory: 19.2 MB
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        l = 0
        r = n - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                arr.append(nums[l] ** 2)
                l += 1
            else:
                arr.append(nums[r]**2)
                r -= 1
        arr.reverse()
        return arr

