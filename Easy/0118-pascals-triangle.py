"""
Problem Name: Pascal's Triangle
Difficulty: Easy
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.6 MB
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        
        for i in range(numRows-1):
            temp = [0] + ret[-1] + [0]
            row = []

            for j in range(len(ret[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            ret.append(row)
        
        return ret

