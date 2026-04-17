"""
Problem Name: Reverse Vowels of a String
Difficulty: Easy
Tags: Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 10 ms
Memory: 18.6 MB
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        
        left, right = 0, len(chars) - 1

        vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}

        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            
            chars[left], chars[right] = chars[right], chars[left]
            
            left += 1
            right -= 1
        
        return ''.join(chars)

