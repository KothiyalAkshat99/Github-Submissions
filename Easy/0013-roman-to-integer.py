"""
Problem Name: Roman to Integer
Difficulty: Easy
Tags: Hash Table, Math, String
"""

"""
Submission 1
Language: python3
Runtime: 52 ms
Memory: 16.5 MB
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        # If (I, X, C) placed BEFORE any LARGER digit, subtraction
        # Else addition
        mydict = {}
        mydict['M'] = 1000
        mydict['D'] = 500
        mydict['C'] = 100
        mydict['L'] = 50
        mydict['X'] = 10
        mydict['V'] = 5
        mydict['I'] = 1

        sum = 0
        i = 0

        while i < len(s):
            # Subtraction Case
            if i+1 < len(s) and mydict[s[i]] < mydict[s[i+1]]:
                sum += mydict[s[i+1]] - mydict[s[i]]
                i += 2
            
            # Not a subtraction case
            else:
                sum += mydict[s[i]]
                i += 1
        
        return sum

"""
Submission 2
Language: python3
Runtime: 10 ms
Memory: 17.9 MB
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ret = 0

        for i, j in zip(s, s[1:]):
            if roman[i] < roman[j]:
                ret -= roman[i]
            else:
                ret += roman[i]
        
        return ret + roman[s[-1]]

