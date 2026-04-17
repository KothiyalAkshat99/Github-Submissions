"""
Problem Name: Island Perimeter
Difficulty: Easy
Tags: Array, Depth-First Search, Breadth-First Search, Matrix
"""

"""
Submission 1
Language: python3
Runtime: 130 ms
Memory: 25 MB
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def pRecur(i, j):
            if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i, j))
            p = pRecur(i, j + 1)
            p += pRecur(i + 1, j)
            p += pRecur(i, j - 1)
            p += pRecur(i - 1, j)

            return p

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return pRecur(i, j)

"""
Submission 2
Language: python3
Runtime: 120 ms
Memory: 35.1 MB
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r: int, c: int) -> int:
            if r == ROWS or c == COLS or \
                r < 0 or c < 0 or \
                grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            
            visited.add((r,c))

            ret = dfs(r, c + 1)
            ret += dfs(r, c - 1)
            ret += dfs(r + 1, c)
            ret += dfs(r - 1, c)

            return ret
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: return dfs(r, c)


