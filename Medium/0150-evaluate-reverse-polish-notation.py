"""
Problem Name: Evaluate Reverse Polish Notation
Difficulty: Medium
Tags: Array, Math, Stack
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 19.1 MB
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #print(tokens)
        stack = []
        for i in tokens:

            if i.lstrip('-+').isdigit():
                stack.append(int(i))
                #print(stack, end = '\n')

            elif i == '+' or i == '-' or i == '*' or i == '/':
                x1 = stack.pop(-1)
                x2 = stack.pop(-1)

                if i == '+':
                    x = x1 + x2
                elif i == '-':
                    x = x2 - x1
                elif i == '*':
                    x = x1 * x2
                elif i == '/':
                    x = int(x2 / x1) if x2 * x1 >= 0 else -(abs(x2) // abs(x1))
                #print(x)
                stack.append(int(x))

            else:
                print(f'{i} invalid')
                continue
        
        return int(stack[0])

