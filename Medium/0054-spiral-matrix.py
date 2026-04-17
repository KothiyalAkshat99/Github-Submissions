"""
Problem Name: Spiral Matrix
Difficulty: Medium
Tags: Array, Matrix, Simulation
"""

"""
Submission 1
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # for every i in top row
            for i in range(left, right):
                ret.append(matrix[top][i])
            top += 1

            # for every i in right col
            for i in range(top, bottom):
                ret.append(matrix[i][right-1])
            right -= 1

            # in case of single row or single cols
            if not (left < right and top < bottom):
                break
            
            # every i in bottom row
            for i in range(right - 1, left - 1, -1):
                ret.append(matrix[bottom-1][i])
            bottom -= 1

            # every i in left col
            for i in range(bottom-1, top-1, -1):
                ret.append(matrix[i][left])
            left += 1
        
        return ret

