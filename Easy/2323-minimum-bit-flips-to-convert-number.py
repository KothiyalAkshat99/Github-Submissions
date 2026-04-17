"""
Problem Name: Minimum Bit Flips to Convert Number
Difficulty: Easy
Tags: Bit Manipulation
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.6 MB
"""
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal # Xor to find differing bits
        count = 0

        while ans:
            # Count incremented if last digit is 1
            count += ans & 1 
            # Shifting answer to right by 1 bit
            ans >>= 1 
        
        return count

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start^goal).bit_count()

