"""
Problem Name: Contains Duplicate II
Difficulty: Easy
Tags: Array, Hash Table, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 9021 ms
Memory: 27.8 MB
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):
            temp = nums[i]

            j = min(i+k, len(nums)-1)

            if temp in nums[i+1:j+1]:
                return True
        
        return False

"""
Submission 2
Language: python3
Runtime: 9037 ms
Memory: 28 MB
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):
            temp = nums[i]

            j = min(i+k, len(nums)-1)

            if temp in nums[i+1:j+1]:
                return True
        
        return False

"""
Submission 3
Language: python3
Runtime: 456 ms
Memory: 28 MB
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        myset = set() # Sliding window set
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                myset.remove(nums[l])
                l += 1
            
            if nums[r] in myset:
                return True

            myset.add(nums[r])
        
        return False

"""
Submission 4
Language: python3
Runtime: 75 ms
Memory: 46.5 MB
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        ret = False

        for i in range(len(nums)):
            num = nums[i]
            if num not in hmap:
                hmap[num] = []
            else:
                if abs(hmap[num][-1] - i) <= k:
                    ret = True
                    break
            hmap[num].append(i)

        return ret

"""
Submission 5
Language: python3
Runtime: 31 ms
Memory: 36.8 MB
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in hmap and abs(hmap[num] - i) <= k:
                return True
            hmap[num] = i
            '''
            if num not in hmap:
                hmap[num] = []
            else:
                if abs(hmap[num][-1] - i) <= k:
                    ret = True
                    break
            hmap[num].append(i)
            '''
        
        return False

