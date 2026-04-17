"""
Problem Name: Maximum Difference by Remapping a Digit
Difficulty: Easy
Tags: Math, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 1 ms
Memory: 17.9 MB
"""
class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        # Max - Find first non 9 digit, replace all occurences with 9
        # Min - Find and replace all occurences of first digit with 0
        
        num = str(num)

        maxd = ''
        for i in num:
            if i != '9':
                maxd = i
                break
        
        maxNum = ''
        for i in num:
            if i == maxd:
                maxNum = maxNum + '9'
            else:
                maxNum = maxNum + i
        
        minNum = ''
        for i in num:
            if i == num[0]:
                minNum = minNum + '0'
            else:
                minNum = minNum + i
        
        return int(maxNum) - int(minNum)

