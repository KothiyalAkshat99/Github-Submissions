"""
Problem Name: Range Sum Query 2D - Immutable
Difficulty: Medium
Tags: Array, Design, Matrix, Prefix Sum
"""

"""
Submission 1
Language: python3
Runtime: 107 ms
Memory: 30.6 MB
"""
class NumMatrix:
    # PREFIX SUM of 
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])

        # Has 1 extra row + col of 0's
        self.sumMat = [[0] * (cols + 1) for r in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # offset according to out new matrix size
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topleft = self.sumMat[row1 - 1][col1 - 1]

        return bottomRight - above - left + topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

