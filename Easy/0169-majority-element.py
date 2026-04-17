"""
Problem Name: Majority Element
Difficulty: Easy
Tags: Array, Hash Table, Divide and Conquer, Sorting, Counting
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.2 MB
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ret = 0
        count = 0

        for i in nums:

            if count == 0: ret = i

            count += (1 if i == ret else -1)

        return ret

"""
Submission 2
Language: python3
Runtime: 7 ms
Memory: 19.4 MB
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initially, set first element to be majority element
        # for each occurence, increase count
        # When we encounter a different number than current majority, DECREASE count
        # If count becomes 0, set new current digit to be majority element

        ret = 0
        count = 0

        for i in nums:

            if count == 0: ret = i

            count += (1 if i == ret else -1)

        return ret

