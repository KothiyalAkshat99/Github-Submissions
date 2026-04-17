"""
Problem Name: Baseball Game
Difficulty: Easy
Tags: Array, Stack, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.9 MB
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for char in operations:
            if char == 'C':
                scores.pop()
            elif char == 'D':
                scores.append(scores[-1] * 2)
            elif char == '+':
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(char))
        
        return sum(scores)

