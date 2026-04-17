"""
Problem Name: Online Stock Span
Difficulty: Medium
Tags: Stack, Design, Monotonic Stack, Data Stream
"""

"""
Submission 1
Language: python3
Runtime: 66 ms
Memory: 23 MB
"""
class StockSpanner:

    def __init__(self):
        # Monotonic stack
        self.stockPrices : List[[price,span]] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stockPrices and self.stockPrices[-1][0] <= price:
            span += self.stockPrices.pop()[1]
        self.stockPrices.append([price, span])
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

