"""
Problem Name: 3Sum
Difficulty: Medium
Tags: Array, Two Pointers, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 618 ms
Memory: 20.6 MB
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums = list(set(nums))
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i>0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = n-1
            while j<k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                else:
                    res.append([nums[i] , nums[j] , nums[k]])
                    j += 1
                    while j<k and nums[j-1] == nums[j]:
                        j += 1

        return res

"""
Submission 2
Language: python3
Runtime: 639 ms
Memory: 20.6 MB
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums = list(set(nums))
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i>0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = n-1
            while j<k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    res.append([nums[i] , nums[j] , nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j-1]==nums[j]:
                        j += 1
                    while j<k and nums[k]==nums[k+1]:
                        k -= 1

        return res

"""
Submission 3
Language: python3
Runtime: 739 ms
Memory: 20.6 MB
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []

        n = len(nums)
        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        
        return ret
                

"""
Submission 4
Language: python3
Runtime: 743 ms
Memory: 20.8 MB
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []

        n = len(nums)
        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
        
        return ret

