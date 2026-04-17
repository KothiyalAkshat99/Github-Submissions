"""
Problem Name: Max Difference You Can Get From Changing an Integer
Difficulty: Medium
Tags: Math, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.6 MB
"""
class Solution:
    def maxDiff(self, num: int) -> int:
        strNum = str(num)
        x, y = '', '9'
        a, b = '', ''
        
        # For Max Number
        for i in strNum:
            if i != '9':
                x = i # Selecting x to be first non 9 digit in given number
                break
        
        for i in strNum:
            if i == x:
                a += y
            else:
                a += i
        
        # For Min Number
        # If First Digit != 1, replace with one.
        # Else, Find first digit (second digit onwards) that's neither 0 not 1, and replace with 0.

        if strNum[0] != '1':
            b = strNum.replace(strNum[0], '1')
        else:
            flag = 0
            for i in strNum:
                if i != '0' and i != '1':
                    b = strNum.replace(i, '0')
                    flag = 1
                    break
            
            if flag == 0:
                b = strNum

        ''' This approach fails since there are leading 0's being considered in this approach.

        # Need to check if number is homogenous
        temp = strNum[0]
        flag = 0 # Homogenous
        for i in strNum:
            if i != temp:
                flag = 1 # Non-homogenous number
                break

        x = strNum[0]

        if flag == 1:    
            y = '0'
        else:
            y = '1'

        for i in strNum:
            if i == x:
                b += y
            else:
                b += i
        '''
        
        return int(a) - int(b)

