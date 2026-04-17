"""
Problem Name: Minimum Length of String After Deleting Similar Ends
Difficulty: Medium
Tags: Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 27 ms
Memory: 18.5 MB
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            c = s[left]
            
            while left <= right and s[left] == c:
                left += 1
            
            while left < right and s[right] == c:
                right -= 1
        
        return right - left + 1

