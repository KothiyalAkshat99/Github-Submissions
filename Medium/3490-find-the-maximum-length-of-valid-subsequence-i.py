"""
Problem Name: Find the Maximum Length of Valid Subsequence I
Difficulty: Medium
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 44 ms
Memory: 39.2 MB
"""
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Valid Subsequence only when all evens, all odds, or alt even odds
        evencount = 0
        oddcount = 0
        altcount = 0
        parity = -1

        for i in nums:
            if i % 2 == 0:
                evencount += 1
                if parity == 1 or parity == -1:
                    altcount += 1
            else:
                oddcount += 1
                if parity == 0 or parity == -1:
                    altcount += 1
            parity = i % 2
        
        return max(altcount, evencount, oddcount)

"""
Submission 2
Language: python3
Runtime: 55 ms
Memory: 39 MB
"""
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Valid Subsequence only when all evens, all odds, or alt even odds
        evencount = 0
        oddcount = 0
        altcount = 0
        parity = -1 # Marks start of array

        for i in nums:
            if i % 2 == 0:                      # Current is Even
                evencount += 1
                if parity == 1 or parity == -1: # Checks if PREVIOUS was odd(1) or START(-1)
                    altcount += 1               # Alt count increases in this case
            else:                               # Current is Odd
                oddcount += 1
                if parity == 0 or parity == -1: # Checks if PREVIOUS was EVEN(0) or START(-1)
                    altcount += 1               # Alt count increases in this case
            parity = i % 2  # Getting parity of current element
        
        return max(altcount, evencount, oddcount)

