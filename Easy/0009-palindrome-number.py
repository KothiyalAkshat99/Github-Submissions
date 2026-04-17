"""
Problem Name: Palindrome Number
Difficulty: Easy
Tags: Math
"""

"""
Submission 1
Language: python3
Runtime: 48 ms
Memory: 16.4 MB
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        srev = s[::-1]
        if s == srev:
            return True
        else:
            return False

"""
Submission 2
Language: python3
Runtime: 44 ms
Memory: 16.5 MB
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

"""
Submission 3
Language: python3
Runtime: 11 ms
Memory: 17.8 MB
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        reverse = 0
        temp = x
        while temp:
            digit = temp % 10
            #print(digit)
            temp = temp//10
            reverse = reverse * 10 + digit
        if reverse == x:
            return True
        else:
            return False

