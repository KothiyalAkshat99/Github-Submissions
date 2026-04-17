"""
Problem Name: Climbing Stairs
Difficulty: Easy
Tags: Math, Dynamic Programming, Memoization
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        
        # JUSTA FIBONACCI SMH

        one, two = 1, 1
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # TOP-DOWN (Memoization) -
        # Introducing a cache to Recursion
        memo = {}
        def dfs(x):
            if x == n or x == n-1:
                return 1
            if x in memo:
                return memo[x]
            memo[x] = dfs(x+1) + dfs(x+2)
            return memo[x]
        
        return dfs(0)

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # BOTTOM-UP -> TABULATION
        if n in (0, 1):
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

"""
Submission 4
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recur(n):
            if n in memo:
                return memo[n]

            if n == 0:
                return 1
            if n < 0:
                return 0
            
            ret = 0
            ret += recur(n - 1) + recur(n - 2)
            
            memo[n] = ret
            
            return ret
        
        return recur(n)

"""
Submission 5
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        memo = [0] * (n + 1)
        memo[0] = memo[1] = 1   # For n = 0 and n = 1, numways = 1 (Base Case solution here)

        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n]

"""
Submission 6
Language: python3
Runtime: 0 ms
Memory: 19.2 MB
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        #memo = [0] * (n + 1)
        #memo[0] = memo[1] = 1   # For n = 0 and n = 1, numways = 1 (Base Case solution here)
        a = b = 1
        c = 0

        for i in range(2, n + 1):
            #memo[i] = memo[i - 1] + memo[i - 2]
            c = b + a
            a = b
            b = c
        
        return c

