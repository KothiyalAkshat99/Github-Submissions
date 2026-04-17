"""
Problem Name: Maximum Average Subarray I
Difficulty: Easy
Tags: Array, Sliding Window
"""

"""
Submission 1
Language: python3
Runtime: 847 ms
Memory: 28.1 MB
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if k > n:
            return
        slidersum = sum(nums[:k])
        maxsum = slidersum
        l = 0
        r = k
        #while r != n:
            #l+=1
            #slidersum = slidersum + nums[r] - nums[l]
            #if slidersum > maxsum:
                #maxsum = slidersum
            #r+=1
        
        for i in range(k, n):
            slidersum = slidersum + nums[i] - nums[i - k]
            #print(slidersum)
            if slidersum > maxsum:
                maxsum = slidersum
        
        maxavg = maxsum / k

        return float(maxavg)

"""
Submission 2
Language: python3
Runtime: 851 ms
Memory: 28.7 MB
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        slidersum = sum(nums[:k])
        maxsum = slidersum
        l = 0
        r = k
        #while r != n:
            #l+=1
            #slidersum = slidersum + nums[r] - nums[l]
            #if slidersum > maxsum:
                #maxsum = slidersum
            #r+=1
        
        for i in range(k, n):
            slidersum = slidersum + nums[i] - nums[i - k]
            #print(slidersum)
            if slidersum > maxsum:
                maxsum = slidersum
        
        maxavg = maxsum / k

        return float(maxavg)

"""
Submission 3
Language: python3
Runtime: 818 ms
Memory: 28.1 MB
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        slidersum = sum(nums[:k])
        maxsum = slidersum

        for i in range(k, len(nums)):
            slidersum = slidersum + nums[i] - nums[i - k]
            #print(slidersum)
            if slidersum > maxsum:
                maxsum = slidersum
        
        maxavg = maxsum / k

        return float(maxavg)

