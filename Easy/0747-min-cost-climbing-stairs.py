"""
Problem Name: Min Cost Climbing Stairs
Difficulty: Easy
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18 MB
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i + 2])
        
        return min(cost[0], cost[1])

"""
Submission 2
Language: python3
Runtime: 9 ms
Memory: 20.1 MB
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top Down Memoization - O(n)
        # Without Memoization - Exponential, TLE - O(2^n)
        if not cost:
            return 0
        n = len(cost)
        memo = {}
        
        def recur(i):
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return cost[i]
            if i in memo: return memo[i]
            
            memo[i] = cost[i] + min(recur(i-1), recur(i-2))
            return memo[i]
        
        return min(recur(n-1), recur(n-2))

"""
Submission 3
Language: python3
Runtime: 3 ms
Memory: 17.8 MB
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost) == 1:
            return ccost[0]
        
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])

"""
Submission 4
Language: python3
Runtime: 3 ms
Memory: 17.6 MB
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]
        
        n = len(cost)
        n1 = cost[0]
        n2 = cost[1]

        for i in range(2, n):
            curr = cost[i] + min(n1, n2)
            n1 = n2
            n2 = curr
        
        return min(n1, n2)

"""
Submission 5
Language: python3
Runtime: 7 ms
Memory: 21.9 MB
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top - Down
        n = len(cost)
        memo = {}

        def recur(i):
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return cost[i]
            
            if i in memo:
                return memo[i]

            ret = cost[i] + min(recur(i - 1), recur(i - 2))
            memo[i] = ret

            return ret
        
        return min(recur(n - 1), recur(n - 2))

"""
Submission 6
Language: python3
Runtime: 3 ms
Memory: 19.3 MB
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top - Down
        n = len(cost)
        memo = {}

        memo[0] = cost[0]
        memo[1] = cost[1]

        for i in range(2, n):
            memo[i] = cost[i] + min(memo[i - 1], memo[i - 2])
        
        return min(memo[n - 1], memo[n - 2])

"""
Submission 7
Language: python3
Runtime: 0 ms
Memory: 19.2 MB
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        #memo = {}

        #memo[0] = cost[0]
        #memo[1] = cost[1]
        a = cost[0]
        b = cost[1]
        c = 0

        for i in range(2, n):
            c = cost[i] + min(a, b)
            a = b
            b = c
        
        return min(a, b)

