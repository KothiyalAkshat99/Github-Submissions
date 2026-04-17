"""
Problem Name: Number of Islands
Difficulty: Medium
Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 322 ms
Memory: 25.4 MB
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and \
                        grid[r][c] == '1' and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                
        return islands

"""
Submission 2
Language: python3
Runtime: 236 ms
Memory: 20 MB
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ret = 0
        rows = len(grid)
        cols = len(grid[0])
        #visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 \
                or r >= rows or c >= cols \
                or grid[r][c] != "1":
                return # or (r, c) in visited

            # visited.add((r,c))
            grid[r][c] = '#'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1": #and (i, j) not in visited:
                    dfs(i, j)
                    ret += 1
        
        return ret

"""
Submission 3
Language: python3
Runtime: 245 ms
Memory: 21.4 MB
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ret = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or c < 0 or \
                r == ROWS or c == COLS or \
                grid[r][c] != '1':
                return 
            
            grid[r][c] = '#'    # Mark '1' as visited ('#')

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    ret += 1
        
        return ret

"""
Submission 4
Language: python3
Runtime: 270 ms
Memory: 26.8 MB
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ret = 0
        visited = set()

        def bfs(r: int, c: int) -> None:
            dq = collections.deque()
            visited.add((r, c)) # Marking current node as visited
            dq.append((r, c))

            while dq:
                row, col = dq.popleft()
                directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < ROWS and 0 <= c < COLS and \
                        grid[r][c] == '1' and (r, c) not in visited:
                        dq.append((r, c))
                        visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    ret += 1
        
        return ret

