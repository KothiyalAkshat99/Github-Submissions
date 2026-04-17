"""
Problem Name: Valid Sudoku
Difficulty: Medium
Tags: Array, Hash Table, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 5 ms
Memory: 17.7 MB
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqrs = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or\
                    board[r][c] in cols[c] or \
                    board[r][c] in sqrs[(r // 3, c // 3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sqrs[(r//3, c//3)].add(board[r][c])
        
        return True

