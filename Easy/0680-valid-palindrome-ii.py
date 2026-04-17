"""
Problem Name: Valid Palindrome II
Difficulty: Easy
Tags: Two Pointers, String, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 33 ms
Memory: 18.1 MB
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skipL = s[left + 1 : right + 1] # Skipping left character
                skipR = s[left : right] # Skipping right character
                
                # Checking if after deleting either left/ right, the result is a palindrome
                # Returns False if not, else just returns True, since no more checks required
                return (skipL == skipL[::-1]) or (skipR == skipR[::-1])
            
            left += 1
            right -= 1
        
        return True

