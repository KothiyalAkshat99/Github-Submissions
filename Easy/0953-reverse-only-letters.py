"""
Problem Name: Reverse Only Letters
Difficulty: Easy
Tags: Two Pointers, String
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 17.9 MB
"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        sArray = list(s)

        while left < right:
            while left < right and not sArray[left].isalpha():
                left += 1
            
            while left < right and not sArray[right].isalpha():
                right -= 1
            
            if left < right:
                sArray[left], sArray[right] = sArray[right], sArray[left]
                left += 1
                right -= 1
        
        return ''.join(sArray)

