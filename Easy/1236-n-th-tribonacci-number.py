"""
Problem Name: N-th Tribonacci Number
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
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        a, b, c = 0, 1, 1
        n -= 2
        x = 0
        while n:
            n -= 1
            x = a + b + c
            a = b
            b = c
            c = x
        
        return x

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19.4 MB
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def recur(i):
            if i in memo:
                return memo[i]
            if i == 1 or i == 2:
                return 1
            if i <= 0:
                return 0
            
            ret = recur(i-1) + recur(i-2) + recur(i-3)
            memo[i] = ret
            return ret
        
        return recur(n)

"""
Submission 3
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        for i in range(3, n + 1):
            ret = memo[i - 1] + memo[i - 2] + memo[i - 3]
            memo[i] = ret
        
        return memo[n]

"""
Submission 4
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        #memo = {}
        #memo[0] = 0
        #memo[1] = 1
        #memo[2] = 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a = 0   # T_0
        b = 1   # T_1
        c = 1   # T_2
        d = 0

        for i in range(3, n + 1):
            d = a + b + c
            a = b
            b = c
            c = d
        
        return d

