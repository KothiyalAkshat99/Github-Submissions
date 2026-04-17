"""
Problem Name: Search a 2D Matrix
Difficulty: Medium
Tags: Array, Binary Search, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 18.4 MB
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            if target == matrix[0][0]:
                return True
            return False
        i = 0

        while(True):
            #print(matrix[i][n-1])
            print(i)
            print(n-1)
            if target > matrix[i][n-1]:
                i += 1
            elif target == matrix[i][n-1]:
                return True
            else:
                break
            if i == m:
                return False
        print(i)
        #return False
        j = 0
        l = n

        while(j<=l):
            k = (j + l) // 2
            if target == matrix[i][k]:
                return True
            elif target > matrix[i][k]:
                j = k + 1
            else:
                l = k - 1
            
        return False

"""
Submission 2
Language: python3
Runtime: 0 ms
Memory: 18.2 MB
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = 0
        l = m - 1

        while(j <= l):
            i = (j + l) // 2
            print(i)
            if target > matrix[i][-1]:
                j = i + 1
            elif target < matrix[i][0]:
                l = i - 1
            else:
                break
        
        if j > l:
            return False
        j = 0
        l = n - 1

        while(j<=l):
            k = (j + l) // 2
            print(k)
            if target < matrix[i][k]:
                l = k - 1
            elif target > matrix[i][k]:
                j = k + 1
            else:
                return True
            
        return False

