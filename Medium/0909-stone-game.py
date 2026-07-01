"""
Problem Name: Stone Game
Difficulty: Medium
Tags: Array, Math, Dynamic Programming, Game Theory
"""

"""
Submission 1
Language: python3
Runtime: 474 ms
Memory: 139 MB
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = {}
        def recur(l: int, r: int) -> tuple:
            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            parity = (r - l - n) % 2

            if parity == 1:
                score1 = recur(l + 1, r) + piles[l]
                score2 = recur(l, r - 1) + piles[r]
                memo[(l, r)] = max(score1, score2)
                return memo[(l, r)]
            
            score1 = recur(l + 1, r) - piles[l]
            score2 = recur(l, r - 1) - piles[r]
            memo[(l, r)] = max(score1, score2)
            return memo[(l, r)]

        ret = recur(0, n - 1)
        return True if ret else 0

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

