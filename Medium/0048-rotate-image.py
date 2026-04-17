"""
Problem Name: Rotate Image
Difficulty: Medium
Tags: Array, Math, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 1 ms
Memory: 17.7 MB
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = rows
        
        # Reverse each column
        r1 = 0
        r2 = rows - 1

        while r1 < r2:
            for c in range(cols):
                temp = matrix[r1][c]
                matrix[r1][c] = matrix[r2][c]
                matrix[r2][c] = temp
            r1 += 1
            r2 -= 1
        
        for r in range(rows):
            for c in range(r+1, cols):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

