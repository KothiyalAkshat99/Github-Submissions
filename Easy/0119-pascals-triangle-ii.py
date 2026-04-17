"""
Problem Name: Pascal's Triangle II
Difficulty: Easy
Tags: Array, Dynamic Programming
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [1]

        for i in range(rowIndex):
            curr_row = [0] * (len(ret)+1) # Current row length = Prev Row Length + 1

            for j in range(len(ret)):
                curr_row[j] += ret[j]
                curr_row[j+1] += ret[j]
            
            ret = curr_row
        
        return ret

