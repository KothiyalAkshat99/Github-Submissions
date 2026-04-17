"""
Problem Name: N-Queens II
Difficulty: Hard
Tags: Backtracking
"""

"""
Submission 1
Language: python3
Runtime: 11 ms
Memory: 19.4 MB
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        
        #board = [["."] * n for row in range(n)]
        ret = 0

        cols = set()
        pstv_diag = set()   # Constant R+C
        ngtv_diag = set()   # Constant R-C

        def backtrack(r: int):
            if r == n:
                nonlocal ret
                ret += 1
                return
            
            for c in range(n):
                if (c in cols) or ((r+c) in pstv_diag) or ((r-c) in ngtv_diag):
                    continue
                
                # Place Queen
                cols.add(c)
                pstv_diag.add(r+c)
                ngtv_diag.add(r-c)
                #board[r][c] = 'Q'

                backtrack(r + 1)

                # Remove Queen (backtrack)
                cols.remove(c)
                pstv_diag.remove(r+c)
                ngtv_diag.remove(r-c)
                #board[r][c] = '.'
        
        backtrack(0)

        return ret

