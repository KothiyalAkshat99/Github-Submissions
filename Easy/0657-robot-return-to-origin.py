"""
Problem Name: Robot Return to Origin
Difficulty: Easy
Tags: String, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.1 MB
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return (moves.count('R') == moves.count('L'))  & (moves.count('U') == moves.count('D'))

