"""
Problem Name: Fizz Buzz
Difficulty: Easy
Tags: Math, String, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 49 ms
Memory: 17.8 MB
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(0,n):
            st = ''
            divby3 = (i+1)%3
            divby5 = (i+1)%5
            if divby3 == 0:
                st+='Fizz'
            if divby5 == 0:
                st+='Buzz'
            
            if st=='':
                arr.append(f'{i+1}')
                continue
            arr.append(st)
        return arr

