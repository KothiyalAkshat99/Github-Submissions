"""
Problem Name: String to Integer (atoi)
Difficulty: Medium
Tags: String
"""

"""
Submission 1
Language: python3
Runtime: 2 ms
Memory: 17.7 MB
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - 2 ** 31

        i = 0
        n = len(s)

        # Skipping leading Whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        if not s:
            return 0
        
        if i == n:
            return 0
        
        # Checking Signs
        flag = 1
        #print(s[i])
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            flag = -1
            i += 1
        
        # Reading digits and converting
        ret = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            ret = ret * 10 + digit
            
            if flag * ret <= INT_MIN:
                return INT_MIN
            if flag * ret >= INT_MAX:
                return INT_MAX
            
            i += 1
            
        return ret * flag
        

