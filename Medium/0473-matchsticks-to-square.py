"""
Problem Name: Matchsticks to Square
Difficulty: Medium
Tags: Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
"""

"""
Submission 1
Language: python3
Runtime: 3636 ms
Memory: 19.6 MB
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4  # Max Length of each side
        sides = [0] * 4

        # If float division != integer division of length
        # I.E. if the array is not divisible into 4 equal integer parts
        if (sum(matchsticks) / 4) != length:
            return False
        
        matchsticks.sort(reverse=True)

        def backtrack(i: int) -> bool:
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            
            return False
        
        return backtrack(0)

"""
Submission 2
Language: python3
Runtime: 3923 ms
Memory: 19.3 MB
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4  # Max Length of each side
        sides = [0] * 4

        # If float division != integer division of length
        # I.E. if the array is not divisible into 4 equal integer parts
        if (sum(matchsticks) / 4) != length or len(matchsticks) < 4:
            return False
        
        matchsticks.sort(reverse=True)

        def backtrack(i: int) -> bool:
            if i == len(matchsticks):
                return True
            
            if matchsticks[i] > length:
                return False
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            
            return False
        
        return backtrack(0)

