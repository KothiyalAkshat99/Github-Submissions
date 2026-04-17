"""
Problem Name: Shortest Distance to Target String in a Circular Array
Difficulty: Easy
Tags: Array, String
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 19.3 MB
"""
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        for step in range(n):
            # Check right (clockwise) and left (counter-clockwise)
            if words[(startIndex + step) % n] == target or \
               words[(startIndex - step + n) % n] == target:
                return step
        return -1

