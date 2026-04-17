"""
Problem Name: Word Search
Difficulty: Medium
Tags: Array, String, Backtracking, Depth-First Search, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 4300 ms
Memory: 18.1 MB
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i): #row, col, current character
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 \
                or r >= rows or c >= cols or \
                word[i] != board[r][c] or \
                (r, c) in path):
                return False
            
            path.add((r, c)) # add visited node to set, as we cannot visit same node twice while finding path.

            res = (dfs(r + 1, c, i + 1) or \
                    dfs(r - 1, c, i + 1) or \
                    dfs(r, c + 1, i + 1) or \
                    dfs(r, c - 1, i + 1))
            
            path.remove((r, c))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False

"""
Submission 2
Language: python3
Runtime: 4352 ms
Memory: 17.8 MB
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i): #row, col, current character
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 \
                or r >= rows or c >= cols or \
                word[i] != board[r][c] or \
                (r, c) in path):
                return False
            
            path.add((r, c)) # add visited node to set, as we cannot visit same node twice while finding path.

            res = (dfs(r + 1, c, i + 1) or \
                    dfs(r - 1, c, i + 1) or \
                    dfs(r, c + 1, i + 1) or \
                    dfs(r, c - 1, i + 1))
            
            path.remove((r, c))

            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0): return True
        return False

"""
Submission 3
Language: python3
Runtime: 4200 ms
Memory: 19.7 MB
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def wordExists(row: int, col: int, idx: int) -> bool:
            # This method searches if current word exists in the board through DFS
            if idx == len(word):
                return True
            
            if row < 0 or row >= rows \
                or col < 0 or col >= cols \
                or board[row][col] != word[idx] \
                or (row, col) in path:
                return False
            
            path.add((row, col))

            ret = wordExists(row + 1, col, idx + 1) or \
                    wordExists(row - 1, col, idx + 1) or \
                    wordExists(row, col + 1, idx + 1) or \
                    wordExists(row, col - 1, idx + 1)
            
            path.remove((row, col))

            return ret


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and wordExists(row, col, 0):
                    return True
        
        return False

"""
Submission 4
Language: python3
Runtime: 3769 ms
Memory: 19.5 MB
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def wordExists(row: int, col: int, idx: int) -> bool:
            # This method searches if current word exists in the board through DFS
            if idx == len(word):
                return True
            
            if row < 0 or row >= rows \
                or col < 0 or col >= cols \
                or board[row][col] != word[idx] \
                or (row, col) in path:
                return False
            
            board[row][col] = '#'   # Marking as visited instead of using a set

            ret = wordExists(row + 1, col, idx + 1) or \
                    wordExists(row - 1, col, idx + 1) or \
                    wordExists(row, col + 1, idx + 1) or \
                    wordExists(row, col - 1, idx + 1)
            
            board[row][col] = word[idx]   # This stands since if they were unequal, fn would've returned at base case already

            return ret


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and wordExists(row, col, 0):
                    return True
        
        return False

"""
Submission 5
Language: python3
Runtime: 3355 ms
Memory: 19.6 MB
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def wordExists(row: int, col: int, idx: int) -> bool:
            # This method searches if current word exists in the board through DFS
            if idx == len(word):
                return True
            
            if row < 0 or row >= rows \
                or col < 0 or col >= cols \
                or board[row][col] != word[idx] \
                or board[row][col] == '#':
                return False
            
            board[row][col] = '#'   # Marking as visited instead of using a set

            ret = wordExists(row + 1, col, idx + 1) or \
                    wordExists(row - 1, col, idx + 1) or \
                    wordExists(row, col + 1, idx + 1) or \
                    wordExists(row, col - 1, idx + 1)
            
            board[row][col] = word[idx]   # This stands since if they were unequal, fn would've returned at base case already

            return ret


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and wordExists(row, col, 0):
                    return True
        
        return False

