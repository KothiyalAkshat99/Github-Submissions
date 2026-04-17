"""
Problem Name: N-Queens
Difficulty: Hard
Tags: Array, Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 13 ms
Memory: 18.2 MB
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return [[]]
        if n == 1:
            return [["Q"]]

        # TRACKING DIAGONALS - 
        # For NEGATIVE diagonals, (r-c) remains constant
        # Eg - (0,0) -> (r-c) = 0
        # Diagonal is (1, 1) -> (r-c) = 0
        # This property remains constant for any and all NEGATIVE diagonals

        # For POSITIVE DIAGONALS - (r+c) remains CONSTANT

        # POSITIVE DIAGONALS (R + C)
        # NEGATIVE DIAGONALS (R - C)
        
        cols = set() # Tracking columns where Queens have been placed
        neg_diag = set() # (R - C)
        pos_diag = set() # (R + C)

        ret = []
        board = [["."] * n for i in range(n)]

        def backTrack(r):
            # Base case, all Queens have been placed
            if r == n:
                copy = ["".join(row) for row in board]
                ret.append(copy)
                return
            
            for c in range(0, n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                backTrack(r + 1)

                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        
        backTrack(0)

        return ret

"""
Submission 2
Language: python3
Runtime: 7 ms
Memory: 19.9 MB
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return [[]]
        if n == 1:
            return [["Q"]]
        
        board = [["."] * n for i in range(n)]
        ret = []

        # No need for row set because we're traversing linearly by row
        cols = set()
        pstv_diag = set()   # Constant R+C
        ngtv_diag = set()   # Constant R-C

        def backtrack(r: int) -> None:
            if r == n:
                temp = ["".join(row) for row in board]
                ret.append(temp)
                return
            
            for c in range(0, n):
                if c in cols or (r+c) in pstv_diag or (r-c) in ngtv_diag:
                    continue
                
                # placing queen at current r,c and marking visited
                cols.add(c)
                pstv_diag.add(r+c)
                ngtv_diag.add(r-c)
                board[r][c] = "Q"

                backtrack(r + 1)    # Going to next row

                # Backtracking
                cols.remove(c)
                pstv_diag.remove(r+c)
                ngtv_diag.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)

        return ret

