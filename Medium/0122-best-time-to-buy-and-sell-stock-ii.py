"""
Problem Name: Best Time to Buy and Sell Stock II
Difficulty: Medium
Tags: Array, Dynamic Programming, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18.7 MB
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit

