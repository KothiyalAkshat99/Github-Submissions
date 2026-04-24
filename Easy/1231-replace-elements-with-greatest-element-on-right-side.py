"""
Problem Name: Replace Elements with Greatest Element on Right Side
Difficulty: Easy
Tags: Array
"""

"""
Submission 1
Language: python3
Runtime: 18 ms
Memory: 20.4 MB
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        n = len(arr)
        curr_max = arr[n - 1]
        
        for i in range(n - 2, -1, -1):
            temp = arr[i]
            arr[i] = curr_max
            if temp > curr_max:
                curr_max = temp
        
        arr[-1] = -1
        return arr

