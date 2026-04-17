"""
Problem Name: Rotating the Box
Difficulty: Medium
Tags: Array, Two Pointers, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 98 ms
Memory: 63.4 MB
"""
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])

        ret = [["." for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            # Process each row in reverse order
            lowest_row_with_empty_cell = cols-1 # The last col processed first (reverse)

            for j in range(cols-1, -1, -1):
                # If stone found, let it fall to lowest empty cell
                if boxGrid[i][j] == "#":
                    ret[lowest_row_with_empty_cell][rows - i - 1] = "#"
                    lowest_row_with_empty_cell -= 1
                
                # If obstacle found, reset lowest empty
                if boxGrid[i][j] == "*":
                    ret[j][rows - i - 1] = "*"
                    lowest_row_with_empty_cell = j-1
        
        return ret

