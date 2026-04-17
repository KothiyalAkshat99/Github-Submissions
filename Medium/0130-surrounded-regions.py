"""
Problem Name: Surrounded Regions
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 4 ms
Memory: 21.5 MB
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # We're gonna start with the First/Last Rows/Cols
        # DFS on any 'O' regions in F/L R/C
        # Mark all of the connected regions as 'C', and these cannot be surrounded
        # Mark all other regions as 'X' inside a m*n loop, marking them as surrounded

        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or\
                r == rows or c == cols or\
                board[r][c] == 'C' or board[r][c] == 'X':
                return
            
            board[r][c] = 'C'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        
        #print(board)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'C':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
        
        return

"""
Submission 2
Language: python3
Runtime: 4 ms
Memory: 22.4 MB
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        not_surrounded = set()

        def dfs(r, c):
            if r < 0 or c < 0 or \
                r == ROWS or c == COLS or \
                board[r][c] == 'X' or (r, c) in not_surrounded:
                return
            
            not_surrounded.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return

        
        # FIRST AND LAST ROW
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        # FIRST AND LAST COL
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in not_surrounded:
                    board[r][c] = 'X'

