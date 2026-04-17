"""
Problem Name: Valid Parentheses
Difficulty: Easy
Tags: String, Stack
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18 MB
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        ret = []
        idx = 0
        for i in s:
            if i == '(' or i == '{' or i == '[':
                ret.append(i)
                #print(ret)
            elif i == ')':
                if len(ret) == 0:
                    return False
                else:
                    x = ret.pop()
                    if x != '(':
                        return False
            elif i == '}':
                if len(ret) == 0:
                    return False
                else:
                    x = ret.pop()
                    if x != '{':
                        return False
            elif i == ']':
                if len(ret) == 0:
                    return False
                else:
                    x = ret.pop()
                    if x != '[':
                        return False
        #print(ret)
        if len(ret) == 0:
            return True
        else:
            return False

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1:
            return False
        
        stk = []
        dic = {}
        dic[')'] = '('
        dic[']'] = '['
        dic['}'] = '{'

        for i in s:
            if i in dic.values():
                stk.append(i) # Adding to top of stack
            elif i in dic.keys():
                if not stk:
                    return False
                temp = stk.pop()
                if temp != dic[i]:
                    return False


        if stk:
            return False
        else:
            return True

