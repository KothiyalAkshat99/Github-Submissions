"""
Problem Name: Richest Customer Wealth
Difficulty: Easy
Tags: Array, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 41 ms
Memory: 16.6 MB
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        global maxsum
        maxsum = 0
        for i in accounts:
            sum=0
            for j in i:
                sum+=j
            if sum>maxsum:
                maxsum = sum
        return maxsum

