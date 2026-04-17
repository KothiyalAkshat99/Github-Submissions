"""
Problem Name: Valid Palindrome
Difficulty: Easy
Tags: Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 50 ms
Memory: 17.2 MB
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        s = s.lower()
        s1 = ""
        for i in s:
            if i.isalnum():
                s1 += i
        return s1==s1[::-1]

"""
Submission 2
Language: python3
Runtime: 14 ms
Memory: 23.3 MB
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True

