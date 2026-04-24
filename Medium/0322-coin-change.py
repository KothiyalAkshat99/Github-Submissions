"""
Problem Name: Coin Change
Difficulty: Medium
Tags: Array, Dynamic Programming, Breadth-First Search
"""

"""
Submission 1
Language: python3
Runtime: 751 ms
Memory: 18.1 MB
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1

"""
Submission 2
Language: python3
Runtime: 1046 ms
Memory: 69.2 MB
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        memo = {}

        def recur(cursum: int) -> int:
            if cursum > amount:
                return -1
            if cursum == amount:
                return 0
            if cursum in memo:
                return memo[cursum]
            
            min_coins = float('inf')

            for coin in coins:
                ret = recur(cursum + coin)
                if ret != -1:
                    min_coins = min(min_coins, 1 + ret)

            memo[cursum] = min_coins if min_coins != float('inf') else -1
            return memo[cursum]
        
        return recur(0)

"""
Submission 3
Language: python3
Runtime: 1100 ms
Memory: 63 MB
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        coins.sort()
        memo = {}

        def recur(cursum: int) -> int:
            if cursum > amount:
                return -1
            if cursum == amount:
                return 0
            if cursum in memo:
                return memo[cursum]
            
            min_coins = float('inf')

            for coin in coins:
                ret = recur(cursum + coin)
                if ret != -1:
                    min_coins = min(min_coins, 1 + ret)

            memo[cursum] = min_coins if min_coins != float('inf') else -1
            return memo[cursum]
        
        return recur(0)

"""
Submission 4
Language: python3
Runtime: 503 ms
Memory: 19.5 MB
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1


        return memo[0]

