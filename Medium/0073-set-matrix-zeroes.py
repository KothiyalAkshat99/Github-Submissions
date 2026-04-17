"""
Problem Name: Set Matrix Zeroes
Difficulty: Medium
Tags: Array, Hash Table, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 3 ms
Memory: 18.5 MB
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1) solution
        rows, cols = len(matrix), len(matrix[0])

        rowZero = False

        # Determine which rows/cols need to be zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        # 0 out all required rows and cols except first
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # 0 out first column if need to
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        # 0 out first row if need to
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0

