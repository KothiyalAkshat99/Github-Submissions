"""
Problem Name: Best Time to Buy and Sell Stock
Difficulty: Easy
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 28 ms
Memory: 26.8 MB
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        
        return profit

"""
Submission 2
Language: python3
Runtime: 41 ms
Memory: 26.7 MB
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1: return 0

        b = prices[0]
        maxpr = 0

        for i in range(1, len(prices)):
            if prices[i] < b:
                b = prices[i]
            elif prices[i] - b > maxpr:
                maxpr = prices[i] - b
        
        return maxpr

